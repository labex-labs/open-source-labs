# Générer des miniatures

Dans cette étape, vous allez générer des miniatures pour toutes les images dans le répertoire spécifié. Vous utiliserez une boucle `for` pour parcourir toutes les images avec l'extension `.png` dans le répertoire spécifié. Pour chaque image, vous allez générer une miniature et la sauvegarder dans le répertoire `thumbs`.

```python
for path in args.imagedir.glob("*.png"):
    outpath = outdir / path.name
    fig = image.thumbnail(path, outpath, scale=0.15)
    print(f"saved thumbnail of {path} to {outpath}")
```
