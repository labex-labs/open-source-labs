# Build and Install

To deploy the Flask application, we need to create a distribution file called a wheel file. Follow the steps below to build and install the application:

1. Install the `build` tool by running the following command:

```bash
$ pip install build
```

2. Build the wheel file using the `build` tool:

```bash
$ python -m build --wheel
```

3. Locate the generated wheel file in the `dist` folder. The file name will be in the format of `{project name}-{version}-{python tag}-{abi tag}-{platform tag}`.

4. Copy the wheel file to the production server.

5. Set up a new virtual environment on the production server.

6. Install the wheel file using `pip`:

```bash
$ pip install flaskr-1.0.0-py3-none-any.whl
```

7. Run the `init-db` command to create the database in the instance folder:

```bash
$ flask --app flaskr init-db
```

Note: If Flask detects that it's installed (not in editable mode), it uses a different directory for the instance folder. You can find it at `.venv/var/flaskr-instance` instead.
