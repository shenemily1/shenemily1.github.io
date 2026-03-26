# Tutorial: Setting Up the Automatic Paper Writing Workflow

This guide walks you through setting up and running the automated end-to-end AI workflow for generating JAMA Network Open papers from datasets.

## Table of Contents
1. [Prerequisites](#prerequisites)
2. [Step 1: Clone the Repository](#step-1-clone-the-repository)
3. [Step 2: Set Up VSCode with Copilot](#step-2-set-up-vscode-with-copilot)
4. [Step 3: Prepare Your Data](#step-3-prepare-your-data)
5. [Step 4: Using Copilot to Generate the Workflow](#step-4-using-copilot-to-generate-the-workflow)
6. [Step 5: View Your Generated Paper](#step-5-view-your-generated-paper)
7. [Advanced: Running the Workflow Manually](#advanced-running-the-workflow-manually)

---

## Prerequisites

Before you begin, make sure you have the following installed:
- **Git** - For cloning the repository
- **Python 3.8+** - For running the workflow scripts
- **VSCode** - For editing and running the workflow
- **GitHub Copilot** - For AI-assisted paper generation (requires VSCode extension)
- **LaTeX** - For compiling the final PDF (pdflatex or similar)

Optional but recommended:
- **Conda** or **Pip** virtual environment for dependency isolation

---

## Step 1: Clone the Repository

### Via Command Line

Open your terminal/command prompt and run:

```bash
git clone https://github.com/hsph-bst236-2026/midterm-project-ele_aaa midterm-project && cd midterm-project && code . -a
```

**What this command does:**
- Clones the repository into a folder named `midterm-project`
- Navigates into the folder (`cd midterm-project`)
- Opens the project in VSCode (`code . -a`)

### Alternative: Manual Steps

If you prefer to do this manually:

1. Go to [https://github.com/hsph-bst236-2026/midterm-project-ele_aaa](https://github.com/hsph-bst236-2026/midterm-project-ele_aaa)
2. Click the green **"Code"** button and select **"Clone with HTTPS"** or **"Clone with SSH"**
3. Copy the URL
4. Open a terminal and run:
   ```bash
   git clone [PASTE_URL] midterm-project
   cd midterm-project
   code . -a
   ```

---

## Step 2: Set Up VSCode with Copilot

### Install GitHub Copilot Extension

1. Open VSCode and navigate to the **Extensions** panel (Ctrl+Shift+X on Windows)
2. Search for **"GitHub Copilot"**
3. Click **Install**
4. Sign in with your GitHub account when prompted

### Verify Installation

- Look for the Copilot icon in the sidebar (should appear as a chat icon)
- You should see a message confirming Copilot is ready to use

---

## Step 3: Prepare Your Data

The workflow expects data in a specific location. This project includes sample data to test with, but you can also add your own.

### Using the Sample Exam Data (Recommended for First Run)

The repository includes a sample dataset in `Midterm_Exam-main/data/`. This folder contains:
- `Data_Description.md` - Description of the datasets
- `hcw_mandates_table.csv` - Healthcare worker mandate data
- `United_States_COVID-19_Cases_and_Deaths_by_State_over_Time...csv` - COVID-19 cases and deaths

These files are already in place and ready to use.

### Using Your Own Data

If you want to use a different dataset:

1. **Create or locate your data folder** - This should contain:
   - One or more CSV/XLSX files with your datasets
   - (Optional) A `Data_Description.md` file explaining your datasets

2. **Copy your data into the project** - You can place it in:
   - `Midterm_Exam-main/data/` (to replace sample data)
   - Or create a new folder like `my_data/` at the project root

3. **Document your data** - Create a `Data_Description.md` file that includes:
   ```markdown
   # Data Description
   
   ## Dataset Overview
   - **File**: your_dataset.csv
   - **Rows**: [number of rows]
   - **Columns**: [list of columns]
   - **Description**: Brief description of what the data contains
   
   ## Variables
   - Variable1: Description
   - Variable2: Description
   ```

---

## Step 4: Using Copilot to Generate the Workflow

### 4a. Open Copilot Chat

1. In VSCode, click on the **Copilot Chat** icon in the left sidebar (or press Ctrl+Shift+I)
2. A chat panel will open on the right side

### 4b. Paste the Copilot Prompt

Copy and paste the following prompt into the Copilot chat:

```
Write a paper using the data in the Midterm_Exam-main folder using the workflow provided by the workflow folder
```

**Alternative prompts you can use:**
- `Generate a JAMA Network Open style paper analyzing the data in Midterm_Exam-main/data/`
- `Create a research paper using the COVID-19 and healthcare mandate datasets in Midterm_Exam-main/data/`

### 4c. Let Copilot Run the Workflow

Copilot will:
1. Analyze the data in the specified folder
2. Perform exploratory data analysis (EDA)
3. Select appropriate statistical models
4. Generate tables and figures
5. Write manuscript sections (Title, Abstract, Methods, Results, Discussion, etc.)
6. Compile everything into a LaTeX document
7. Generate a PDF paper

**Processing time**: Expect 2-5 minutes depending on dataset size and complexity.

### Monitor Progress

Copilot will provide updates as it completes each step. You can watch the workflow progress in the chat.

---

## Step 5: View Your Generated Paper

### 5a. Using Copilot CLI (Recommended)

Once the workflow completes, type this into the Copilot chat:

```
Open the paper in explorer
```

This will:
- Open the file explorer
- Navigate to the output folder (`output/paper.pdf`)
- Display your generated paper

### 5b. Manual Navigation

If the above doesn't work, manually navigate to the paper:

1. In VSCode file explorer (left panel), go to: `output/` folder
2. Look for `paper.pdf`
3. Double-click to open and view your paper

### 5c. Locate Paper Outputs

The complete paper generation outputs are saved in:

```
output/
├── paper.pdf              ← Your final paper
└── paper_summary.html     ← Web version summary

manuscript/
├── title.txt
├── abstract.txt
├── introduction.txt
├── methods.txt
├── results.txt
├── discussion.txt
├── limitations.txt
└── conclusion.txt

results/
├── figures/
│   ├── figure1.png
│   ├── figure2.png
│   └── ...
├── tables/
│   ├── table1.csv
│   ├── table2.csv
│   └── ...
└── models/
    └── analysis_results.json

derived_data/
├── main_analysis_data.csv      ← Processed dataset
├── eda_summary.json            ← Data exploration results
├── dataset_inventory.json      ← File inventory
├── analysis_plan.json          ← Selected analysis variables
└── variable_roles.json         ← Variable classifications
```

---

## Advanced: Running the Workflow Manually

If you want more control over the workflow or need to debug, you can run the workflow manually from the terminal.

### 5a. Open Terminal in VSCode

1. Press Ctrl+` (backtick) or go to **Terminal** → **New Terminal**
2. Make sure you're in the project root directory (`midterm-project`)

### 5b. Run the Workflow

Run the following command (all on one line):

```bash
python workflow/run_workflow.py --input_dir Midterm_Exam-main --project_root . --authors "Your Name; Team Member 1; Team Member 2"
```

**Parameters:**
- `--input_dir` - Path to your data folder (e.g., `Midterm_Exam-main`, `my_data/`, `sample/`)
- `--project_root` - Root directory of the project (usually `.` for current directory)
- `--authors` - Semicolon-separated list of author names (optional)

### 5c. Alternative Commands

**Run with sample data (default):**
```bash
python workflow/run_workflow.py --input_dir sample --project_root .
```

**Run with exam data:**
```bash
python workflow/run_workflow.py --input_dir Midterm_Exam-main --project_root .
```

**Skip pre-flight checks (for debugging):**
```bash
python workflow/run_workflow.py --input_dir Midterm_Exam-main --project_root . --skip_preflight
```

### 5d. Monitor Workflow Progress

The workflow logs progress to:
- **Console output** - Real-time messages in the terminal
- **Log files** - Detailed logs saved in `results/logs/`

To view logs after completion:
```bash
cat results/logs/main_dataset_log.json
cat results/logs/data_description_log.json
```

---

## Troubleshooting

### Issue: "Module not found" error

**Solution:** Install required Python packages:
```bash
pip install pandas numpy matplotlib statsmodels scipy
```

### Issue: LaTeX compilation fails

**Solution:** Make sure you have LaTeX installed. If not:
- **Windows**: Install MiKTeX or TeX Live
- **Mac**: Install MacTeX
- **Linux**: `sudo apt-get install texlive-full`

### Issue: Copilot doesn't recognize the prompt

**Solution:** Make sure:
1. GitHub Copilot extension is installed
2. You're logged in to GitHub
3. The chat panel is active
4. The path `Midterm_Exam-main/data/` contains CSV files

### Issue: Paper PDF won't open

**Solution:** 
1. Check if `output/paper.pdf` exists
2. Try viewing in a different PDF viewer
3. Check workflow logs: `results/logs/quality_review_report.json`

### Issue: Workflow takes too long

**Solution:**
- Use a smaller dataset for testing
- Check your internet connection (for LLM API calls)
- Increase timeout in configuration if needed

---

## Complete Workflow Summary

Here's the complete 10-step automated process:

| Step | Name | Input | Output |
|------|------|-------|--------|
| 1 | File Detection | Data folder | `dataset_inventory.json` |
| 2 | Data Selection | Inventory + Description | `main_analysis_data.csv` |
| 3 | Exploratory Data Analysis | Main dataset | `eda_summary.json`, `variable_roles.json` |
| 4 | Analysis Planning | EDA results | `analysis_plan.json` |
| 5 | Statistical Analysis | Dataset + Plan | Tables, model results |
| 6 | Visualization | Results | Figures (PNG/PDF) |
| 7 | Manuscript Writing | All results | Manuscript sections (TXT) |
| 7.5 | Quality Review | Manuscript | Formatting checks |
| 8 | LaTeX Building | Manuscript + Template | `paper.tex` |
| 9 | PDF Compilation | LaTeX file | `paper.pdf` |

---

## Next Steps

- Customize author names and paper metadata
- Adjust figure and table layouts
- Add your own research questions in the analysis plan
- Modify the LaTeX template for different journal styles
- Extend the workflow with domain-specific analyses

---

## Support & Resources

- **GitHub Issues**: Report bugs at [the repository](https://github.com/hsph-bst236-2026/midterm-project-ele_aaa/issues)
- **Documentation**: See [IMPLEMENTATION_PLAN.md](IMPLEMENTATION_PLAN.md) for technical details
- **Sample Data**: Available in `sample/data/` and `Midterm_Exam-main/data/`
- **Template**: JAMA template at `sample/tex/template.tex`

---

## Quick Reference Card

```bash
# Clone and open
git clone https://github.com/hsph-bst236-2026/midterm-project-ele_aaa midterm-project && cd midterm-project && code . -a

# Run workflow manually
python workflow/run_workflow.py --input_dir Midterm_Exam-main --project_root .

# View final paper
# In VSCode: output/paper.pdf

# View manuscript sections
# In VSCode: manuscript/ folder

# View logs
cat results/logs/*.json
```

---

## Video Tutorial

For a visual walkthrough, see the video tutorial at:
https://shenemily1.github.io/tutorial.mp4

---

Happy paper writing! 📝✨
