# Analizar argumentos

En este paso, analizarás los argumentos pasados a tu programa. Debes crear un objeto `ArgumentParser` y agregar un argumento llamado `imagedir`. Este argumento especifica la ruta al directorio que contiene las imágenes. Puedes usar el parámetro `type` para especificar el tipo de datos del argumento. En este caso, el argumento debe ser del tipo `Path`.

```python
parser = ArgumentParser(description="Build thumbnails of all images in a directory.")
parser.add_argument("imagedir", type=Path)
args = parser.parse_args()
```
