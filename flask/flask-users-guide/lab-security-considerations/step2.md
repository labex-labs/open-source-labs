# Cross-Site Request Forgery (CSRF)

Cross-Site Request Forgery (CSRF) is an attack that tricks users into performing unintended actions on a website. To prevent CSRF attacks in Flask, follow these guidelines:

- Use one-time tokens to validate requests that modify server content.
- Store the token in the cookie and transmit it with form data.
- Compare the token received on the server with the one stored in the cookie.

Example code:

```python
# app.py

from flask import Flask, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'secret_key'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/delete', methods=['POST'])
def delete_user():
    if request.method == 'POST':
        token = request.form.get('token')
        if token and token == session.get('csrf_token'):
            # Delete user profile
            return redirect(url_for('index'))
    return 'Invalid request'

if __name__ == '__main__':
    app.run()
```

To run the code, save it in a file called `app.py` and execute the command `flask run`.
