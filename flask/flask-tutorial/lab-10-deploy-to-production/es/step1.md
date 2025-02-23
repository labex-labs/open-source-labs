# Construir la aplicación

Primero, necesitamos crear un archivo wheel para nuestra aplicación. Para esto, usaremos la herramienta `build`. Instala la herramienta `build` con pip si aún no la has instalado:

```bash
# Instala la herramienta build
pip install build
```

Ahora, usa la herramienta `build` para crear el archivo wheel:

```bash
# Construye el archivo wheel
python -m build --wheel
```

El archivo wheel debería estar en el directorio `dist` con un nombre como `flaskr-1.0.0-py3-none-any.whl`.
