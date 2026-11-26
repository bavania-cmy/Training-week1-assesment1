# Training-week1-assesment1
week-1 tasks under this repo
# Week 1 - Python & Data Engineering Assessment

## Project Structure
- `data/`: Raw employee and department CSVs along with generated JSON and high-earner outputs.
- `src/: Core Python OOP/exception logic (task1.py) and CSV/JSON/API client scripts (task2.py`).
- `notebooks/: Jupyter notebook (week_analysis.ipynb) and exported script (week_analysis.py`).
- `reports/: Saved Matplotlib visualizations (chart1` through `chart4`).

## Setup Steps
1. Clone the repository: `git clone https://github.com`
2. Navigate into the folder: `cd Ai-training-week1-assessment`
3. Create and activate a virtual environment: `python -m venv .venv` then `.\.venv\Scripts\Activate.ps1`
4. Install dependencies: `pip install -r requirements.txt`
5. Copy `.env.example` to `.env` and set your `API
6. Run `python src/task1.py, ``python src/task2.py, and execute ``notebooks/week_analysis.ipynb`.

## Summary of Findings
- Out of 8 employees across 4 active departments, 5 earn above 50,000 INR and 4 are based in Chennai.
- Finance leads in average monthly salary at 90,000 INR, followed by IT at 67,667 INR across 3 staff members.
- Outer merging `employees.csv` with `departments.csv` revealed that the Marketing department currently has zero employees.
- Cleaning `employees_dirty.csv` by imputing missing salaries with the median and dropping 1 duplicate restored data integrity.
- External REST API calls handled connection and 404 errors cleanly while parsing nested user records safely.
"@ | Set-Content -Encoding UTF8 README.md
