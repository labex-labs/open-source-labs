# Agregando plantillas HTML

Flask utiliza plantillas Jinja2 para generar contenido HTML. Vamos a crear un archivo de plantilla y renderizarlo en nuestra ruta.

1. Crea un nuevo directorio en tu proyecto llamado `templates`.

2. Dentro del directorio `templates`, crea un nuevo archivo llamado `index.html`.

3. Abre el archivo `index.html` y agrega el siguiente código HTML:

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

4. Modifica tu archivo `app.py` para renderizar la plantilla `index.html`:

   ```python
   from flask import render_template

   @app.route("/")
   def hello_world():
       return render_template("index.html")
   ```
