# Gerar Miniaturas

Nesta etapa, você gerará miniaturas para todas as imagens no diretório especificado. Você usará um loop `for` para iterar sobre todas as imagens com a extensão `.png` no diretório especificado. Para cada imagem, você gerará uma miniatura e a salvará no diretório `thumbs`.

```python
for path in args.imagedir.glob("*.png"):
    outpath = outdir / path.name
    fig = image.thumbnail(path, outpath, scale=0.15)
    print(f"saved thumbnail of {path} to {outpath}")
```
