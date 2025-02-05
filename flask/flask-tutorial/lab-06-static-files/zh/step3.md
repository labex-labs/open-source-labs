# 在 HTML 中链接 CSS 文件

现在，我们需要在 HTML 模板中链接我们的 CSS 文件。Flask 会自动添加一个用于提供静态文件的 `static` 视图。我们可以在 `base.html` 模板中使用 `url_for` 函数来链接我们的 CSS 文件。

```html+jinja
<!-- base.html -->

{{ url_for('static', filename='style.css') }}
```
