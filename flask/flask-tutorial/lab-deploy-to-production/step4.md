# Run the Application with a Production Server

For a production environment, you should use a WSGI server instead of the built-in development server. We will use Waitress as our WSGI server.

First, install Waitress:

```bash
# Install Waitress
pip install waitress
```

Now, tell Waitress to serve your application:

```bash
# Run the application with Waitress
waitress-serve --call 'flaskr:create_app'
```
