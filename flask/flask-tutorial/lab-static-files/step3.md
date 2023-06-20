# Link the CSS file in the base.html template

1. Open the `base.html` file in the `templates` directory.
2. Locate the `<head>` section of the HTML file.
3. Add the following line of code inside the `<head>` section:

```html+jinja
<link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
```
