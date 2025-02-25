# Vérifier une propriété

Créez une fonction appelée `check_prop` qui prend deux paramètres : `fn` et `prop`. Le paramètre `fn` est une fonction prédicat qui sera appliquée à la propriété spécifiée d'un dictionnaire. Le paramètre `prop` est une chaîne de caractères qui représente le nom de la propriété à laquelle la fonction prédicat sera appliquée.

La fonction `check_prop` devrait renvoyer une fonction lambda qui prend un dictionnaire et applique la fonction prédicat, `fn`, à la propriété spécifiée.

```python
def check_prop(fn, prop):
  return lambda obj: fn(obj[prop])
```

```python
check_age = check_prop(lambda x: x >= 18, 'age')
user = {'name': 'Mark', 'age': 18}
check_age(user) # True
```
