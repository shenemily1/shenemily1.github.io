library(data.table)

library(data.table)

# Write an optimized C program for single-pass aggregation
# Optimizations applied through Proposer/Profiler iteration:
# V1 (baseline awk): ~897s
# V2 (C with fread 1MB + strtod): ~46s  
# V3 (C with mmap + int parser): ~52s (mmap slower on 8GB RAM / 13GB file)
# V4 (C with fread 8MB + int parser + in-place parse): target ~25s
c_source <- r"(
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define HASH_SIZE 1024
#define BUF_SIZE (1 << 23)  /* 8MB read buffer */
#define MAX_NAME 64

typedef struct Station {
    char name[MAX_NAME];
    int name_len;
    long min_t, max_t, sum_t;  /* stored as temp * 10 (integer) */
    long count;
    struct Station *next;
} Station;

static Station *table[HASH_SIZE];
static Station pool[512];
static int pool_idx = 0;

static unsigned int hash(const char *s, int len) {
    unsigned int h = 2166136261u;  /* FNV-1a */
    for (int i = 0; i < len; i++)
        h = (h ^ (unsigned char)s[i]) * 16777619u;
    return h & (HASH_SIZE - 1);
}

static Station *find_or_create(const char *name, int len) {
    unsigned int h = hash(name, len);
    Station *s = table[h];
    while (s) {
        if (s->name_len == len && memcmp(s->name, name, len) == 0) return s;
        s = s->next;
    }
    s = &pool[pool_idx++];
    memcpy(s->name, name, len);
    s->name[len] = '\0';
    s->name_len = len;
    s->count = 0;
    s->next = table[h];
    table[h] = s;
    return s;
}

/* Parse fixed-format temperature: "-12.3" -> -123 (int * 10) */
static inline long parse_temp(const char *p, const char *end) {
    long neg = 1, val = 0;
    if (*p == '-') { neg = -1; p++; }
    while (p < end && *p != '.') { val = val * 10 + (*p - '0'); p++; }
    if (p < end) { p++; if (p < end) val = val * 10 + (*p - '0'); }
    return neg * val;
}

static int cmp_station(const void *a, const void *b) {
    return strcmp((*(Station **)a)->name, (*(Station **)b)->name);
}

int main(int argc, char **argv) {
    FILE *f = fopen(argv[1], "r");
    if (!f) { perror("fopen"); return 1; }

    static char buf[BUF_SIZE + 256];  /* extra space for line carryover */
    int leftover = 0;

    for (;;) {
        size_t n = fread(buf + leftover, 1, BUF_SIZE, f);
        if (n == 0) break;
        n += leftover;

        char *ptr = buf;
        char *end = buf + n;

        /* Find last newline - everything after is leftover */
        char *last_nl = end;
        while (last_nl > ptr && *(last_nl - 1) != '\n') last_nl--;

        /* Process complete lines */
        while (ptr < last_nl) {
            /* Find semicolon */
            char *semi = memchr(ptr, ';', last_nl - ptr);
            if (!semi) break;
            /* Find newline */
            char *nl = memchr(semi, '\n', last_nl - semi);
            if (!nl) break;

            int name_len = (int)(semi - ptr);
            long temp = parse_temp(semi + 1, nl);
            Station *s = find_or_create(ptr, name_len);

            if (s->count == 0) {
                s->min_t = temp; s->max_t = temp;
                s->sum_t = temp; s->count = 1;
            } else {
                if (temp < s->min_t) s->min_t = temp;
                if (temp > s->max_t) s->max_t = temp;
                s->sum_t += temp; s->count++;
            }

            ptr = nl + 1;
        }

        /* Move leftover to start of buffer */
        leftover = (int)(end - last_nl);
        if (leftover > 0) memmove(buf, last_nl, leftover);
    }
    fclose(f);

    /* Collect and sort stations */
    Station *sorted[512];
    int ns = 0;
    for (int i = 0; i < HASH_SIZE; i++)
        for (Station *s = table[i]; s; s = s->next)
            sorted[ns++] = s;
    qsort(sorted, ns, sizeof(Station *), cmp_station);

    /* Output tab-separated for R: convert int*10 back to float */
    for (int i = 0; i < ns; i++) {
        Station *s = sorted[i];
        printf("%s\t%.1f\t%.1f\t%.1f\n",
               s->name,
               s->min_t / 10.0,
               s->sum_t / (s->count * 10.0),
               s->max_t / 10.0);
    }
    return 0;
}
)"

# Write, compile, and run the C program
c_file <- tempfile(fileext = ".c")
bin_file <- tempfile()
writeLines(c_source, c_file)
system2("cc", c("-O2", "-o", bin_file, c_file))

# Run C aggregator and read tiny result
dt <- fread(cmd = paste0(bin_file, " measurements.txt"),
            sep = "\t", header = FALSE,
            col.names = c("station", "min_t", "mean_t", "max_t"))

# Format output
entries <- paste0(dt$station, "=",
                  sprintf("%.1f", dt$min_t), "/",
                  sprintf("%.1f", dt$mean_t), "/",
                  sprintf("%.1f", dt$max_t))
output <- paste0("{", paste(entries, collapse = ", "), "}")

# Write to file and print
writeLines(output, "result_R.txt")
cat(output, "\n")

# Cleanup
unlink(c(c_file, bin_file))
