# Creando una ruta básica

Las rutas en Flask definen los patrones de URL para tu aplicación. Vamos a crear una ruta básica que muestre un mensaje "¡Hola, Mundo!".

1. Agrega el siguiente código a tu archivo `app.py`:

   ```python
   @app.route("/")
   def hello_world():
       return "Hello, World!"
   ```

2. Guarda el archivo.
