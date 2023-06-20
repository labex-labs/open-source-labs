# Link CSS file in HTML

Now, we need to link our CSS file in the HTML templates. Flask automatically adds a `static` view that serves static files. We can use the `url_for` function in the `base.html` template to link our CSS file.

```html+jinja
<!-- base.html -->

{{ url_for('static', filename='style.css') }}
```
