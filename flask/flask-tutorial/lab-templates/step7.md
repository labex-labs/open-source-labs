# Update the Flask application

Update the `app.py` file to render the child template. Replace the `index` function with the following code:

```python
from flask import render_template

@app.route('/')
def index():
    return render_template('child.html')
```
