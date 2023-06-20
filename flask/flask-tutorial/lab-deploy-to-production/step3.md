# Run with a Production Server

Running the Flask application with the built-in development server is not recommended for production environments. Instead, use a production WSGI server like `Waitress`. Follow the steps below to run the application with Waitress:

1. Install Waitress in the virtual environment:

```bash
$ pip install waitress
```

2. Use the following command to start the Waitress server and specify the application to run:

```bash
$ waitress-serve --call 'flaskr:create_app'
```

The server will start running and listening on a specific address (e.g., `http://0.0.0.0:8080`).
