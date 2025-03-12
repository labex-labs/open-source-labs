# Implémentation de la gestion des exceptions

Dans cette étape, nous allons nous concentrer sur la mise en œuvre de la gestion des exceptions pour rendre votre code plus robuste. Lorsqu'un programme rencontre des données erronées, il a souvent tendance à planter. Cependant, nous pouvons utiliser une technique appelée gestion des exceptions pour gérer ces problèmes de manière élégante. Vous allez modifier le fichier `reader.py` pour implémenter cela. La gestion des exceptions permet à votre programme de continuer à fonctionner même lorsqu'il rencontre des données inattendues, au lieu de s'arrêter brusquement.

## Comprendre les blocs try - except

Python offre un moyen puissant de gérer les exceptions en utilisant des blocs try - except. Analysons comment ils fonctionnent.

```python
try:
    # Code qui peut provoquer une exception
    result = risky_operation()
except SomeExceptionType as e:
    # Code qui s'exécute si l'exception se produit
    handle_exception(e)
```

Dans le bloc `try`, vous placez le code qui peut lever une exception. Une exception est une erreur qui se produit lors de l'exécution d'un programme. Par exemple, si vous essayez de diviser un nombre par zéro, Python lèvera une exception `ZeroDivisionError`. Lorsqu'une exception se produit dans le bloc `try`, Python arrête l'exécution du code dans le bloc `try` et saute au bloc `except` correspondant. Le bloc `except` contient le code qui gérera l'exception. `SomeExceptionType` est le type d'exception que vous souhaitez capturer. Vous pouvez capturer des types d'exceptions spécifiques ou utiliser une exception générale `Exception` pour capturer tous les types d'exceptions. La partie `as e` vous permet d'accéder à l'objet exception, qui contient des informations sur l'erreur.

## Modification du code

Maintenant, appliquons ce que nous avons appris sur les blocs try - except à la fonction `convert_csv()`. Ouvrez le fichier `reader.py` dans votre éditeur.

1. Remplacez la fonction `convert_csv()` actuelle par le code suivant :

```python
def convert_csv(rows, converter, header=True):
    """
    Convert a sequence of rows to an output sequence according to a conversion function.
    """
    if header:
        headers = next(rows)
    else:
        headers = []

    result = []
    for row_idx, row in enumerate(rows, start=1):
        try:
            # Try to convert the row
            result.append(converter(headers, row))
        except Exception as e:
            # Print a warning message for bad rows
            print(f"Row {row_idx}: Bad row: {row}")
            continue

    return result
```

Dans cette nouvelle implémentation :

- Nous utilisons une boucle `for` au lieu de `map()` pour traiter chaque ligne. Cela nous donne plus de contrôle sur le traitement de chaque ligne.
- Nous enveloppons le code de conversion dans un bloc try - except. Cela signifie que si une exception se produit lors de la conversion d'une ligne, le programme ne plantera pas. Au lieu de cela, il saute au bloc `except`.
- Dans le bloc `except`, nous affichons un message d'erreur pour les lignes invalides. Cela nous aide à identifier les lignes qui présentent des problèmes.
- Après avoir affiché le message d'erreur, nous utilisons l'instruction `continue` pour sauter la ligne actuelle et continuer le traitement des lignes restantes.

Enregistrez le fichier après avoir apporté ces modifications.

## Test de vos modifications

Testons votre code modifié avec le fichier `missing.csv`. Tout d'abord, ouvrez l'interpréteur Python en exécutant la commande suivante dans votre terminal :

```bash
python3
```

Une fois que vous êtes dans l'interpréteur Python, exécutez le code suivant :

```python
from reader import read_csv_as_dicts
port = read_csv_as_dicts('missing.csv', types=[str, int, float])
print(f"Number of valid rows processed: {len(port)}")
```

Lorsque vous exécutez ce code, vous devriez voir des messages d'erreur pour chaque ligne problématique. Mais le programme continuera le traitement et retournera les lignes valides. Voici un exemple de ce que vous pourriez voir :

```
Row 4: Bad row: ['C', '', '53.08']
Row 7: Bad row: ['DIS', '50', 'N/A']
Row 8: Bad row: ['GE', '', '37.23']
Row 13: Bad row: ['INTC', '', '21.84']
Row 17: Bad row: ['MCD', '', '51.11']
Row 19: Bad row: ['MO', '', '70.09']
Row 22: Bad row: ['PFE', '', '26.40']
Row 26: Bad row: ['VZ', '', '42.92']
Number of valid rows processed: 20
```

Vérifions également que le programme fonctionne correctement avec des données valides. Exécutez le code suivant dans l'interpréteur Python :

```python
valid_port = read_csv_as_dicts('valid.csv', types=[str, int, float])
print(f"Number of valid rows processed: {len(valid_port)}")
```

Vous devriez constater que toutes les lignes sont traitées sans erreur. Voici un exemple de sortie :

```
Number of valid rows processed: 17
```

Pour quitter l'interpréteur Python, exécutez la commande suivante :

```python
exit()
```

Maintenant, votre code est plus robuste. Il peut gérer les données invalides de manière élégante en sautant les lignes erronées au lieu de planter. Cela rend votre programme plus fiable et plus convivial.
