# Organize the Project

As your project grows, it is recommended to organize your code into packages. Set up your project directory to contain the following:

- `flaskr/`: a Python package containing your application code and files.
- `tests/`: a directory containing test modules.
- `.venv/`: a Python virtual environment where Flask and other dependencies are installed.

```bash
/home/user/Projects/flask-tutorial
├── flaskr/
│ ├── __init__.py
│ ├── db.py
│ ├── schema.sql
│ ├── auth.py
│ ├── blog.py
│ ├── templates/
│ │ ├── base.html
│ │ ├── auth/
│ │ │ ├── login.html
│ │ │ └── register.html
│ │ └── blog/
│ │ ├── create.html
│ │ ├── index.html
│ │ └── update.html
│ └── static/
│ └── style.css
├── tests/
│ ├── conftest.py
│ ├── data.sql
│ ├── test_factory.py
│ ├── test_db.py
│ ├── test_auth.py
│ └── test_blog.py
├── .venv/
├── pyproject.toml
└── MANIFEST.in
```
