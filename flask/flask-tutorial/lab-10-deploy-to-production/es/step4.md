# Ejecutar la aplicación con un servidor de producción

Para un entorno de producción, deberías usar un servidor WSGI en lugar del servidor de desarrollo integrado. Usaremos Waitress como nuestro servidor WSGI.

Primero, instala Waitress:

```bash
# Instala Waitress
pip install waitress
```

Ahora, indica a Waitress que sirva tu aplicación:

```bash
# Ejecuta la aplicación con Waitress
waitress-serve --call 'flaskr:create_app'
```
