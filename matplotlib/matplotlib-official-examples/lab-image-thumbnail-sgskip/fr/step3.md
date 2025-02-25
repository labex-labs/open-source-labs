# Analyser les arguments

Dans cette étape, vous allez analyser les arguments passés à votre programme. Vous devez créer un objet `ArgumentParser` et ajouter un argument nommé `imagedir`. Cet argument spécifie le chemin vers le répertoire contenant les images. Vous pouvez utiliser le paramètre `type` pour spécifier le type de données de l'argument. Dans ce cas, l'argument doit être de type `Path`.

```python
parser = ArgumentParser(description="Build thumbnails of all images in a directory.")
parser.add_argument("imagedir", type=Path)
args = parser.parse_args()
```
