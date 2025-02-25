# Vérifier une propriété

## Problème

Créez une fonction appelée `check_prop` qui prend deux paramètres : `fn` et `prop`. Le paramètre `fn` est une fonction prédicat qui sera appliquée à la propriété spécifiée d'un dictionnaire. Le paramètre `prop` est une chaîne de caractères qui représente le nom de la propriété à laquelle la fonction prédicat sera appliquée.

La fonction `check_prop` devrait renvoyer une fonction lambda qui prend un dictionnaire et applique la fonction prédicat, `fn`, à la propriété spécifiée.

## Exemple

```python
check_age = check_prop(lambda x: x >= 18, 'age')
user = {'name': 'Mark', 'age': 18}
check_age(user) # True
```

Dans l'exemple ci-dessus, nous créons une fonction `check_age` qui vérifie si la valeur de la propriété `age` dans un dictionnaire est supérieure ou égale à 18. Nous créons ensuite un dictionnaire `user` avec une propriété `name` et `age`. Enfin, nous appelons la fonction `check_age` avec le dictionnaire `user` en tant qu'argument, ce qui renvoie `True` car la propriété `age` est égale à 18.
