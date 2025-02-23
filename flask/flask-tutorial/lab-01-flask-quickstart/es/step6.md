# Agregando contenido dinámico

Flask nos permite pasar contenido dinámico a nuestras plantillas. Vamos a modificar nuestra ruta para pasar un parámetro de nombre y mostrar un saludo personalizado.

1. Modifica tu archivo `app.py` para aceptar un parámetro de nombre en la ruta:

   ```python
   @app.route("/<name>")
   def hello(name):
       return render_template("index.html", name=name)
   ```

2. Abre el archivo `index.html` y modifica la etiqueta `<h1>` para mostrar el saludo personalizado:

   ```html
   <h1>Hello, {{ name }}!</h1>
   ```
