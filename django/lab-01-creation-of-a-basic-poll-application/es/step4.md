# Creando la aplicación de encuestas

Ahora que tu entorno, es decir, un "proyecto", está configurado, ya estás listo para comenzar a trabajar.

Cada aplicación que escribas en Django consiste en un paquete de Python que sigue cierta convención. Django viene con una utilidad que genera automáticamente la estructura básica de directorios de una aplicación, de modo que puedas centrarte en escribir código en lugar de crear directorios.

> Proyectos vs. aplicaciones
> ¿Cuál es la diferencia entre un proyecto y una aplicación? Una aplicación es una aplicación web que hace algo, por ejemplo, un sistema de blogs, una base de datos de registros públicos o una pequeña aplicación de encuestas. Un proyecto es una colección de configuraciones y aplicaciones para un sitio web en particular. Un proyecto puede contener múltiples aplicaciones. Una aplicación puede estar en múltiples proyectos.

Tus aplicaciones pueden estar ubicadas en cualquier lugar de tu `ruta de Python <tut-searchpath>`. En este tutorial, crearemos nuestra aplicación de encuestas en el mismo directorio que tu archivo `manage.py` para que se pueda importar como su propio módulo de nivel superior, en lugar de un submódulo de `mysite`.

Para crear tu aplicación, asegúrate de estar en el mismo directorio que `manage.py` y escribe este comando:

```bash
cd ~/project/mysite
python manage.py startapp polls
```

Eso creará un directorio `polls`, que está estructurado de la siguiente manera:

```plaintext
polls/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    views.py
```

Esta estructura de directorios albergará la aplicación de encuestas.
