# Définir la fonction de police

Dans cette étape, nous allons définir une fonction qui définit la police. Cette fonction prend le nom d'une police en argument et renvoie une chaîne de caractères qui définit la police sur le nom spécifié.

```python
def setfont(font):
    return rf'\font\a {font} at 14pt\a '
```
