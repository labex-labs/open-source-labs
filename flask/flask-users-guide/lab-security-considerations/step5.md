# Set-Cookie Options

When setting cookies in Flask, it's important to consider security options to protect sensitive data. Some recommended options are:

- Secure: Limits cookies to HTTPS traffic only.
- HttpOnly: Protects the contents of cookies from being read with JavaScript.
- SameSite: Restricts how cookies are sent with requests from external sites.

Example code:

```python
# app.py

from flask import Flask, make_response

app = Flask(__name__)

@app.route('/')
def index():
    response = make_response('Hello, world!')
    response.set_cookie('username', 'flask', secure=True, httponly=True, samesite='Lax')
    return response

if __name__ == '__main__':
    app.run()
```

To run the code, save it in a file called `app.py` and execute the command `flask run`.
