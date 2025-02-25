# Créer le répertoire de sortie

Dans cette étape, vous allez créer un répertoire nommé `thumbs` où les miniatures seront enregistrées. Si le répertoire existe déjà, il ne sera pas créé à nouveau.

```python
outdir = Path("thumbs")
outdir.mkdir(parents=True, exist_ok=True)
```
