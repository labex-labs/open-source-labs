# Configurando la aplicación

En el mismo archivo `__init__.py`, agrega los detalles de configuración necesarios para tu aplicación. Esto incluye configurar una clave secreta y especificar la ubicación del archivo de base de datos.

```python
# flaskr/__init__.py

# Más código arriba...

if test_config is None:
    # carga la configuración de instancia, si existe, cuando no se está probando
    app.config.from_pyfile('config.py', silent=True)
else:
    # carga la configuración de prueba si se pasa como parámetro
    app.config.from_mapping(test_config)

# asegúrate de que la carpeta de instancia exista
try:
    os.makedirs(app.instance_path)
except OSError:
    pass

# una página simple que dice hola
@app.route('/')
def hello():
    return 'Hello, World!'
```
