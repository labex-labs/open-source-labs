# Set Up Version Control (Optional)

It is recommended to use version control for your projects. Initialize a Git repository and create a `.gitignore` file to exclude unnecessary files:

```shell
$ git init
$ touch .gitignore
```

Add the following content to the `.gitignore` file:

```
.venv/
*.pyc
__pycache__/
instance/
.pytest_cache/
.coverage
htmlcov/
dist/
build/
*.egg-info/
```
