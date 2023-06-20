# Install the Project

Next, we will use `pip` to install the project in the virtual environment.

Run the following command in your terminal:

```none
pip install -e .
```

This tells pip to find `pyproject.toml` in the current directory and install the project in editable or development mode. Editable mode means that as you make changes to your local code, you'll only need to re-install if you change the project's metadata.

To verify the installation, use the `pip list` command:

```none
pip list
```

The output should show the installed project and its dependencies.
