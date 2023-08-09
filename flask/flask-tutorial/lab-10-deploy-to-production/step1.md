# Build the Application

First, we need to create a wheel file for our application. We will use the `build` tool for this. Install the `build` tool using pip if you haven't already:

```bash
# Install the build tool
pip install build
```

Now, use the `build` tool to create the wheel file:

```bash
# Build the wheel file
python -m build --wheel
```

The wheel file should be in the `dist` directory with a name like `flaskr-1.0.0-py3-none-any.whl`.
