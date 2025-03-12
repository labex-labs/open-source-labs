# Comprendre le passage d'arguments de fonction

En Python, les fonctions sont un concept fondamental qui vous permet de regrouper un ensemble d'instructions pour effectuer une tâche spécifique. Lorsque vous appelez une fonction, vous devez souvent lui fournir des données, que nous appelons des arguments. Python propose différentes manières de passer ces arguments aux fonctions. Cette flexibilité est incroyablement utile car elle vous aide à écrire un code plus propre et plus maintenable. Avant d'appliquer ces techniques à notre projet, examinons de plus près ces conventions de passage d'arguments.

## Créer une sauvegarde de votre travail

Avant de commencer à apporter des modifications à notre fichier `stock.py`, il est recommandé de créer une sauvegarde. Ainsi, si quelque chose se passe mal lors de nos expériences, nous pouvons toujours revenir à la version originale. Pour créer une sauvegarde, ouvrez un terminal et exécutez la commande suivante :

```bash
cp stock.py orig_stock.py
```

Cette commande utilise la commande `cp` (copier) dans le terminal. Elle prend le fichier `stock.py` et en crée une copie nommée `orig_stock.py`. En faisant cela, nous nous assurons que notre travail original est sauvegardé en toute sécurité.

## Explorer le passage d'arguments de fonction

En Python, il existe plusieurs façons d'appeler des fonctions avec différents types d'arguments. Explorons en détail chaque méthode.

### 1. Arguments positionnels

La manière la plus simple de passer des arguments à une fonction est par position. Lorsque vous définissez une fonction, vous spécifiez une liste de paramètres. Lorsque vous appelez la fonction, vous fournissez des valeurs pour ces paramètres dans le même ordre que celui de leur définition.

Voici un exemple :

```python
def calculate(x, y, z):
    return x + y + z

# Appel avec des arguments positionnels
result = calculate(1, 2, 3)
print(result)  # Sortie : 6
```

Dans cet exemple, la fonction `calculate` prend trois paramètres : `x`, `y` et `z`. Lorsque nous appelons la fonction avec `calculate(1, 2, 3)`, la valeur `1` est assignée à `x`, `2` est assignée à `y` et `3` est assignée à `z`. La fonction additionne ensuite ces valeurs et renvoie le résultat.

### 2. Arguments nommés (Keyword Arguments)

En plus des arguments positionnels, vous pouvez également spécifier des arguments par leur nom. Cela s'appelle l'utilisation d'arguments nommés. Lorsque vous utilisez des arguments nommés, vous n'avez pas à vous soucier de l'ordre des arguments.

Voici un exemple :

```python
# Appel avec un mélange d'arguments positionnels et nommés
result = calculate(1, z=3, y=2)
print(result)  # Sortie : 6
```

Dans cet exemple, nous passons d'abord l'argument positionnel `1` pour `x`. Ensuite, nous utilisons des arguments nommés pour spécifier les valeurs de `y` et `z`. L'ordre des arguments nommés n'a pas d'importance, tant que vous fournissez les noms corrects.

### 3. Désempilement de séquences et de dictionnaires

Python propose un moyen pratique de passer des séquences et des dictionnaires en tant qu'arguments en utilisant la syntaxe `*` et `**`. Cela s'appelle le désempilement (unpacking).

Voici un exemple de désempilement d'un tuple en arguments positionnels :

```python
# Désempilement d'un tuple en arguments positionnels
args = (1, 2, 3)
result = calculate(*args)
print(result)  # Sortie : 6
```

Dans cet exemple, nous avons un tuple `args` qui contient les valeurs `1`, `2` et `3`. Lorsque nous utilisons l'opérateur `*` avant `args` dans l'appel de fonction, Python désempile le tuple et passe ses éléments en tant qu'arguments positionnels à la fonction `calculate`.

Voici un exemple de désempilement d'un dictionnaire en arguments nommés :

```python
# Désempilement d'un dictionnaire en arguments nommés
kwargs = {'y': 2, 'z': 3}
result = calculate(1, **kwargs)
print(result)  # Sortie : 6
```

Dans cet exemple, nous avons un dictionnaire `kwargs` qui contient les paires clé-valeur `'y': 2` et `'z': 3`. Lorsque nous utilisons l'opérateur `**` avant `kwargs` dans l'appel de fonction, Python désempile le dictionnaire et passe ses paires clé-valeur en tant qu'arguments nommés à la fonction `calculate`.

### 4. Accepter un nombre variable d'arguments

Parfois, vous pouvez vouloir définir une fonction qui peut accepter un nombre quelconque d'arguments. Python vous permet de le faire en utilisant la syntaxe `*` et `**` dans la définition de la fonction.

Voici un exemple d'une fonction qui accepte un nombre quelconque d'arguments positionnels :

```python
# Accepter un nombre quelconque d'arguments positionnels
def sum_all(*args):
    return sum(args)

print(sum_all(1, 2))           # Sortie : 3
print(sum_all(1, 2, 3, 4, 5))  # Sortie : 15
```

Dans cet exemple, la fonction `sum_all` utilise le paramètre `*args` pour accepter un nombre quelconque d'arguments positionnels. L'opérateur `*` collecte tous les arguments positionnels dans un tuple nommé `args`. La fonction utilise ensuite la fonction intégrée `sum` pour additionner tous les éléments du tuple.

Voici un exemple d'une fonction qui accepte un nombre quelconque d'arguments nommés :

```python
# Accepter un nombre quelconque d'arguments nommés
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Python", year=1991)
# Sortie :
# name: Python
# year: 1991
```

Dans cet exemple, la fonction `print_info` utilise le paramètre `**kwargs` pour accepter un nombre quelconque d'arguments nommés. L'opérateur `**` collecte tous les arguments nommés dans un dictionnaire nommé `kwargs`. La fonction itère ensuite sur les paires clé-valeur du dictionnaire et les affiche.

Ces techniques nous aideront à créer des structures de code plus flexibles et réutilisables dans les étapes suivantes. Pour vous familiariser avec ces concepts, ouvrons l'interpréteur Python et essayons quelques-uns de ces exemples.

```bash
python3
```

Une fois que vous êtes dans l'interpréteur Python, essayez d'entrer les exemples ci-dessus. Cela vous donnera une expérience pratique des techniques de passage d'arguments.
