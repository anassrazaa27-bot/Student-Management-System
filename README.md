# Student Performance Management System

A beginner-friendly Python command-line application for maintaining student marks, calculating averages and grades, searching student records, and identifying the top performer. Built as a Junior Python Developer internship-style project.

## Business problem

Managing marks manually in spreadsheets can lead to calculation mistakes, scattered records, and slow reporting. This application centralizes each student's five subject marks and calculates their performance automatically.

## Features

- Register students with a unique student ID and name
- Store marks for English, Mathematics, Computer, Physics, and Chemistry
- Validate marks from 0 to 100
- Calculate total, average, and grade automatically
- Search for a student by ID
- Identify the highest-average student
- List all students
- Persist records in `data/students.csv`

## Grade scale

| Average | Grade |
|---:|:---:|
| 90–100 | A+ |
| 80–89.99 | A |
| 70–79.99 | B |
| 60–69.99 | C |
| 50–59.99 | D |
| 0–49.99 | F |

## Requirements

- Python 3.9 or newer
- No third-party packages are required

## Run the application

Open a terminal in the project folder and run:

```bash
python run.py
```

On some Windows installations, use:

```powershell
py run.py
```

The menu opens in the terminal. Select an option and follow the prompts. Student records are saved automatically to `data/students.csv`.

## Run tests

```bash
python -m unittest discover -s tests -v
```

## Project structure

```text
student-performance-system/
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── student.py
│   └── grading.py
├── data/
│   └── students.csv
├── tests/
│   ├── __init__.py
│   └── test_grading.py
├── screenshots/
├── run.py
├── README.md
├── requirements.txt
├── .gitignore
└── LICENSE
```

## Design overview

- `student.py`: Student data model and CSV repository (read, save, and search).
- `grading.py`: One focused function containing the grade policy.
- `main.py`: Terminal menu, input validation, reports, and top-performer logic.
- `run.py`: Root-level one-command launcher.
- `tests/test_grading.py`: Automated tests for grade boundaries and invalid values.

## Data and privacy note

The sample CSV starts empty. Use fictional student data while testing. Real student records may contain personal information: do not publish them in a public repository. A production deployment should use access controls, authentication, encrypted storage and backups, audit logs, and the university's data-retention policy.

## Contributing

1. Fork the repository.
2. Create a branch: `git checkout -b feature/your-change`.
3. Make a focused change and add tests.
4. Run `python -m unittest discover -s tests -v`.
5. Commit with a descriptive message.
6. Open a pull request describing the change.

## Example commit messages

- `feat: add student registration`
- `feat: calculate grades and averages`
- `test: cover grade boundaries`
- `docs: add setup and usage instructions`

## License

This project is licensed under the MIT License. See `LICENSE`.
