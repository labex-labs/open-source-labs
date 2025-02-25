# Crear el directorio de salida

En este paso, crearás un directorio llamado `thumbs` donde se guardarán las miniaturas. Si el directorio ya existe, no se creará de nuevo.

```python
outdir = Path("thumbs")
outdir.mkdir(parents=True, exist_ok=True)
```
