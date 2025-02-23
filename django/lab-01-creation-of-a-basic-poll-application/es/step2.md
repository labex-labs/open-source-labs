# Creando un proyecto

Si es la primera vez que utilizas Django, tendrás que hacer una configuración inicial. Es decir, necesitarás generar automáticamente un código que establece un `proyecto` de Django, una colección de configuraciones para una instancia de Django, que incluye la configuración de la base de datos, opciones específicas de Django y configuraciones específicas de la aplicación.

Desde la línea de comandos, `cd` a un directorio donde desees almacenar tu código, luego ejecuta el siguiente comando:

```bash
cd ~/project
django-admin startproject mysite
```

Esto creará un directorio `mysite` en tu directorio actual.

Veamos lo que creó `startproject`:

```plaintext
mysite/
    manage.py
    mysite/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
```

Estos archivos son:

- El directorio raíz externo `mysite/` es un contenedor para tu proyecto. Su nombre no importa para Django; puedes renombrarlo como desees.
- `manage.py`: Una utilidad de línea de comandos que te permite interactuar con este proyecto de Django de varias maneras.
- El directorio interno `mysite/` es el paquete de Python real para tu proyecto. Su nombre es el nombre del paquete de Python que necesitarás utilizar para importar cualquier cosa dentro de él (por ejemplo, `mysite.urls`).
- `mysite/__init__.py`: Un archivo vacío que le dice a Python que este directorio debe considerarse un paquete de Python.
- `mysite/settings.py`: Configuraciones/Configuración para este proyecto de Django.
- `mysite/urls.py`: Las declaraciones de URL para este proyecto de Django; una "tabla de contenidos" de tu sitio basado en Django.
- `mysite/asgi.py`: Un punto de entrada para servidores web compatibles con ASGI para servir tu proyecto.
- `mysite/wsgi.py`: Un punto de entrada para servidores web compatibles con WSGI para servir tu proyecto.
