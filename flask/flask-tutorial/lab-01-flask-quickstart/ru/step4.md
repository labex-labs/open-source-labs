# Добавление HTML - шаблонов

Flask использует шаблоны Jinja2 для генерации HTML - содержимого. Создадим файл с шаблоном и выведем его в нашем маршруте.

1. Создайте новую директорию в своем проекте под названием `templates`.

2. Внутри директории `templates` создайте новый файл под названием `index.html`.

3. Откройте файл `index.html` и добавьте следующий HTML - код:

   ```html
   <!doctype html>
   <html>
     <head>
       <title>Flask Quickstart</title>
     </head>
     <body>
       <h1>Hello, Flask!</h1>
     </body>
   </html>
   ```

4. Измените файл `app.py`, чтобы вывести шаблон `index.html`:

   ```python
   from flask import render_template

   @app.route("/")
   def hello_world():
       return render_template("index.html")
   ```
