# Utilisation de la fonction `map()`

En Python, une fonction de haut niveau (Higher-Order Function) est une fonction qui peut prendre une autre fonction comme argument ou renvoyer une fonction en résultat. La fonction `map()` de Python est un excellent exemple de fonction de haut niveau. C'est un outil puissant qui vous permet d'appliquer une fonction donnée à chaque élément d'un itérable, comme une liste ou un tuple. Après avoir appliqué la fonction à chaque élément, elle renvoie un itérateur des résultats. Cette fonctionnalité rend `map()` parfait pour le traitement de séquences de données, comme les lignes d'un fichier CSV.

La syntaxe de base de la fonction `map()` est la suivante :

```python
map(function, iterable, ...)
```

Ici, la `function` est l'opération que vous souhaitez effectuer sur chaque élément de l'`iterable`. L'`iterable` est une séquence d'éléments, comme une liste ou un tuple.

Regardons un exemple simple. Supposons que vous ayez une liste de nombres et que vous souhaitiez élever chaque nombre de cette liste au carré. Vous pouvez utiliser la fonction `map()` pour y parvenir. Voici comment vous pouvez le faire :

```python
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x * x, numbers))
print(squared)  # Output: [1, 4, 9, 16, 25]
```

Dans cet exemple, nous définissons d'abord une liste appelée `numbers`. Ensuite, nous utilisons la fonction `map()`. La fonction `lambda` `lambda x: x * x` est l'opération que nous souhaitons effectuer sur chaque élément de la liste `numbers`. La fonction `map()` applique cette fonction `lambda` à chaque nombre de la liste. Comme `map()` renvoie un itérateur, nous le convertissons en une liste à l'aide de la fonction `list()`. Enfin, nous affichons la liste `squared`, qui contient les valeurs au carré des nombres originaux.

Maintenant, regardons comment nous pouvons utiliser la fonction `map()` pour modifier notre fonction `convert_csv()`. Précédemment, nous avons utilisé une boucle `for` pour itérer sur les lignes des données CSV. Maintenant, nous allons remplacer cette boucle `for` par la fonction `map()`.

```python
def convert_csv(lines, conversion_func, *, headers=None):
    '''
    Convert lines of CSV data using the provided conversion function
    '''
    rows = csv.reader(lines)
    if headers is None:
        headers = next(rows)

    # Use map to apply conversion_func to each row
    records = list(map(lambda row: conversion_func(headers, row), rows))
    return records
```

Cette version mise à jour de la fonction `convert_csv()` fait exactement la même chose que la version précédente, mais elle utilise la fonction `map()` au lieu d'une boucle `for`. La fonction `lambda` à l'intérieur de `map()` prend chaque ligne des données CSV et applique la `conversion_func` à elle, ainsi qu'aux en-têtes.

Testons cette fonction mise à jour pour nous assurer qu'elle fonctionne correctement. Tout d'abord, ouvrez votre terminal et accédez au répertoire du projet. Ensuite, lancez l'interpréteur Python interactif avec le fichier `reader.py`.

```bash
cd ~/project
python3 -i reader.py
```

Une fois que vous êtes dans l'interpréteur Python, exécutez le code suivant pour tester la fonction `convert_csv()` mise à jour :

```python
# Test the updated convert_csv function
with open('portfolio.csv') as f:
    result = convert_csv(f, make_dict)
print(result[0])  # Should print the first dictionary

# Test that csv_as_dicts still works
with open('portfolio.csv') as f:
    portfolio = csv_as_dicts(f, [str, int, float])
print(portfolio[0])  # Should print the first dictionary with converted types
```

Après avoir exécuté ce code, vous devriez voir une sortie similaire à ceci :

```
{'name': 'AA', 'shares': '100', 'price': '32.20'}
{'name': 'AA', 'shares': 100, 'price': 32.2}
```

Cette sortie montre que la fonction `convert_csv()` mise à jour utilisant la fonction `map()` fonctionne correctement, et que les fonctions qui en dépendent continuent également de fonctionner comme prévu.

L'utilisation de la fonction `map()` présente plusieurs avantages :

1. Elle peut être plus concise qu'une boucle `for`. Au lieu d'écrire plusieurs lignes de code pour une boucle `for`, vous pouvez obtenir le même résultat en une seule ligne en utilisant `map()`.
2. Elle communique clairement votre intention de transformer chaque élément d'une séquence. Lorsque vous voyez `map()`, vous savez immédiatement que vous appliquez une fonction à chaque élément d'un itérable.
3. Elle peut être plus économe en mémoire car elle renvoie un itérateur. Un itérateur génère les valeurs à la volée, ce qui signifie qu'il ne stocke pas tous les résultats en mémoire à la fois. Dans notre exemple, nous avons converti l'itérateur renvoyé par `map()` en une liste, mais dans certains cas, vous pouvez travailler directement avec l'itérateur pour économiser de la mémoire.

Pour quitter l'interpréteur Python, vous pouvez taper `exit()` ou appuyer sur Ctrl + D.
