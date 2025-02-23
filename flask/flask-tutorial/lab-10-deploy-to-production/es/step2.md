# Instalar la aplicación en el servidor

Copia el archivo wheel en tu servidor. Una vez que esté allí, configura un nuevo entorno virtual de Python e instala el archivo wheel con pip:

```bash
# Instala el archivo wheel
pip install flaskr-1.0.0-py3-none-any.whl
```

Como este es un nuevo entorno, necesitas inicializar la base de datos nuevamente:

```bash
# Inicializa la base de datos
flask --app flaskr init-db
```
