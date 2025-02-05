# Cross-Site Scripting (XSS)

Cross-Site Scripting (XSS) is a vulnerability that allows attackers to inject malicious scripts into web pages viewed by users. To prevent XSS attacks in Flask, follow these guidelines:

- Always escape text to prevent the inclusion of arbitrary HTML tags.
- Be cautious when generating HTML without the help of Jinja2 templates.
- Use the `Markup` class to escape user-submitted data.
- Avoid sending out HTML or text files from uploaded files.

Example code:

```python
# app.py

from flask import Flask, render_template_string, Markup

app = Flask(__name__)

@app.route('/')
def index():
    value = '<script>alert("XSS Attack")</script>'
    safe_value = Markup.escape(value)
    return render_template_string('<input value="{{ value }}">', value=safe_value)
```

To run the code, save it in a file called `app.py` and execute the command `flask run`.
