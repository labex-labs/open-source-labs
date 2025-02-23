# Incluir archivos necesarios

El backend de compilación de setuptools necesita otro archivo llamado `MANIFEST.in` para incluir archivos no Python en el proyecto.

Crea un `MANIFEST.in` con el siguiente contenido:

```none
# MANIFEST.in

include flaskr/schema.sql
graft flaskr/static
graft flaskr/templates
global-exclude *.pyc
```

Esto le indica a la compilación que copie todo en los directorios `static` y `templates`, y el archivo `schema.sql`, mientras que excluye todos los archivos de bytecode.
