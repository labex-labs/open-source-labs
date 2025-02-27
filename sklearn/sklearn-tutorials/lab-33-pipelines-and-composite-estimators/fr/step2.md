# Paramètres imbriqués

Vous pouvez accéder aux paramètres des estimateurs dans un pipeline en utilisant la syntaxe `<estimateur>__<paramètre>`. Cela est utile pour effectuer des recherches de grille sur les paramètres de tous les estimateurs dans le pipeline. Voici un exemple :

```python
pipe.set_params(clf__C=10)
```
