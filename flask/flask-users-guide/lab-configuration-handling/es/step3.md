# Configuración a partir de archivos

Codificar los valores de configuración en el código no es ideal, especialmente para información sensible. Flask proporciona una forma de cargar la configuración a partir de archivos separados. Crea un nuevo archivo llamado `config.py` y agrega el siguiente código:

```python
DEBUG = False
SECRET_KEY = 'myothersecretkey'
```

En el archivo `app.py`, reemplaza el código de configuración anterior con el siguiente:

```python
app.config.from_object('config')
```

El método `from_object` carga la configuración desde el módulo `config`. Ahora, los valores de `DEBUG` y `SECRET_KEY` se cargarán desde el archivo `config.py`.

Reinicie la aplicación Flask y visite `http://localhost:5000` para ver el mensaje actualizado con los nuevos valores de configuración.
