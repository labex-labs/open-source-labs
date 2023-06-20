# Install the Application on the Server

Copy the wheel file to your server. Once it's there, set up a new Python virtual environment and install the wheel file using pip:

```bash
# Install the wheel file
pip install flaskr-1.0.0-py3-none-any.whl
```

Since this is a new environment, you need to initialize the database again:

```bash
# Initialize the database
flask --app flaskr init-db
```
