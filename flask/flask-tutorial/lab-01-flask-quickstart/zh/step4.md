# 添加 HTML 模板

Flask 使用 Jinja2 模板来生成 HTML 内容。让我们创建一个模板文件并在路由中渲染它。

1. 在你的项目中创建一个名为 `templates` 的新目录。
2. 在 `templates` 目录内，创建一个名为 `index.html` 的新文件。
3. 打开 `index.html` 文件并添加以下 HTML 代码：

   ```html
   <!doctype html>
   <html>
     <head>
       <title>Flask 快速入门</title>
     </head>
     <body>
       <h1>你好，Flask！</h1>
     </body>
   </html>
   ```

4. 修改你的 `app.py` 文件以渲染 `index.html` 模板：

   ```python
   from flask import render_template

   @app.route("/")
   def hello_world():
       return render_template("index.html")
   ```
