# Configuración basada en el entorno

Es común tener diferentes configuraciones para diferentes entornos, como desarrollo, producción y pruebas. Flask te permite cambiar la configuración según variables de entorno. Crea un nuevo archivo llamado `config_dev.py` y agrega el siguiente código:

```python
DEBUG = True
SECRET_KEY = 'devsecretkey'
```

Crea otro archivo llamado `config_prod.py` con el siguiente código:

```python
DEBUG = False
SECRET_KEY = 'prodsecretkey'
```

En el archivo `app.py`, reemplaza el código de configuración anterior con el siguiente:

```python
import os

if os.environ.get('FLASK_ENV') == 'production':
    app.config.from_object('config_prod')
else:
    app.config.from_object('config_dev')
```

La variable de entorno `FLASK_ENV` se utiliza para determinar el entorno. Si se establece en `'production'`, se cargará la configuración de producción; de lo contrario, se cargará la configuración de desarrollo.

Establece la variable de entorno `FLASK_ENV` en `'production'` y reinicia la aplicación Flask. Visita `http://localhost:5000` para ver el mensaje actualizado con los valores de configuración de producción.
