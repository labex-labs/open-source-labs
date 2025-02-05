# Running the Development Server from Python

In addition to using the Flask CLI command, you can also start the development server from Python code. Add the following code at the end of your `app.py` file:

```python
if __name__ == "__main__":
    app.run(debug=True)
```

Now, you can run the development server by executing the `app.py` file with Python:

```bash
python app.py
```

This will start the development server and you can access your Flask application in the same way as before.
