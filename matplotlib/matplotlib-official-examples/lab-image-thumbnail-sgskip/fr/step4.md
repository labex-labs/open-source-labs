# Vérifier le répertoire

Dans cette étape, vous allez vérifier si le répertoire spécifié existe. Si le répertoire n'existe pas, vous allez quitter le programme et afficher un message d'erreur.

```python
if not args.imagedir.is_dir():
    sys.exit(f"Could not find input directory {args.imagedir}")
```
