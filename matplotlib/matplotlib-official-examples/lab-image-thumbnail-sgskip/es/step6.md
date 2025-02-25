# Generar miniaturas

En este paso, generarás miniaturas para todas las imágenes en el directorio especificado. Utilizarás un bucle `for` para iterar sobre todas las imágenes con la extensión `.png` en el directorio especificado. Para cada imagen, generarás una miniatura y la guardarás en el directorio `thumbs`.

```python
for path in args.imagedir.glob("*.png"):
    outpath = outdir / path.name
    fig = image.thumbnail(path, outpath, scale=0.15)
    print(f"saved thumbnail of {path} to {outpath}")
```
