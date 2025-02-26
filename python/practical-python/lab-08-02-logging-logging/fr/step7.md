# Exercice 8.2 : Ajout de la journalisation à un module

Dans `fileparse.py`, il y a une gestion d'erreurs liée aux exceptions causées par des entrées invalides. Elle ressemble à ceci :

```python
# fileparse.py
import csv

def parse_csv(lines, select=None, types=None, has_headers=True, delimiter=',', silence_errors=False):
    '''
    Analyser un fichier CSV en une liste d'enregistrements avec conversion de type.
    '''
    if select and not has_headers:
        raise RuntimeError('select nécessite des en-têtes de colonne')

    rows = csv.reader(lines, delimiter=delimiter)

    # Lire les en-têtes du fichier (s'il y en a)
    headers = next(rows) if has_headers else []

    # Si des colonnes spécifiques ont été sélectionnées, créer des indices pour le filtrage et définir les colonnes de sortie
    if select:
        indices = [ headers.index(colname) for colname in select ]
        headers = select

    records = []
    for rowno, row in enumerate(rows, 1):
        if not row:     # Ignorer les lignes sans données
            continue

        # Si des indices de colonne spécifiques sont sélectionnés, les extraire
        if select:
            row = [ row[index] for index in indices]

        # Appliquer la conversion de type à la ligne
        if types:
            try:
                row = [func(val) for func, val in zip(types, row)]
            except ValueError as e:
                if not silence_errors:
                    print(f"Ligne {rowno}: Impossible de convertir {row}")
                    print(f"Ligne {rowno}: Raison {e}")
                continue

        # Créer un dictionnaire ou un tuple
        if headers:
            record = dict(zip(headers, row))
        else:
            record = tuple(row)
        records.append(record)

    return records
```

Remarquez les instructions `print` qui émettent des messages de diagnostic. Remplacer ces `print` par des opérations de journalisation est relativement simple. Modifiez le code comme ceci :

```python
# fileparse.py
import csv
import logging
log = logging.getLogger(__name__)

def parse_csv(lines, select=None, types=None, has_headers=True, delimiter=',', silence_errors=False):
    '''
    Analyser un fichier CSV en une liste d'enregistrements avec conversion de type.
    '''
    if select and not has_headers:
        raise RuntimeError('select nécessite des en-têtes de colonne')

    rows = csv.reader(lines, delimiter=delimiter)

    # Lire les en-têtes du fichier (s'il y en a)
    headers = next(rows) if has_headers else []

    # Si des colonnes spécifiques ont été sélectionnées, créer des indices pour le filtrage et définir les colonnes de sortie
    if select:
        indices = [ headers.index(colname) for colname in select ]
        headers = select

    records = []
    for rowno, row in enumerate(rows, 1):
        if not row:     # Ignorer les lignes sans données
            continue

        # Si des indices de colonne spécifiques sont sélectionnés, les extraire
        if select:
            row = [ row[index] for index in indices]

        # Appliquer la conversion de type à la ligne
        if types:
            try:
                row = [func(val) for func, val in zip(types, row)]
            except ValueError as e:
                if not silence_errors:
                    log.warning("Ligne %d: Impossible de convertir %s", rowno, row)
                    log.debug("Ligne %d: Raison %s", rowno, e)
                continue

        # Créer un dictionnaire ou un tuple
        if headers:
            record = dict(zip(headers, row))
        else:
            record = tuple(row)
        records.append(record)

    return records
```

Maintenant que vous avez effectué ces modifications, essayez d'utiliser un peu de votre code avec des données invalides.

```python
>>> import report
>>> a = report.read_portfolio('missing.csv')
Ligne 4: Mauvaise ligne : ['MSFT', '', '51.23']
Ligne 7: Mauvaise ligne : ['IBM', '', '70.44']
>>>
```

Si vous ne faites rien, vous ne recevrez que les messages de journalisation pour le niveau `WARNING` et supérieur. La sortie ressemblera à des instructions `print` simples. Cependant, si vous configurez le module de journalisation, vous recevrez des informations supplémentaires sur les niveaux de journalisation, le module, etc. Tapez ces étapes pour voir cela :

```python
>>> import logging
>>> logging.basicConfig()
>>> a = report.read_portfolio('missing.csv')
AVERTISSEMENT:fileparse:Ligne 4: Mauvaise ligne : ['MSFT', '', '51.23']
AVERTISSEMENT:fileparse:Ligne 7: Mauvaise ligne : ['IBM', '', '70.44']
>>>
```

Vous remarquerez que vous ne voyez pas la sortie de l'opération `log.debug()`. Tapez ceci pour changer le niveau.

```python
>>> logging.getLogger('fileparse').setLevel(logging.DEBUG)
>>> a = report.read_portfolio('missing.csv')
AVERTISSEMENT:fileparse:Ligne 4: Mauvaise ligne : ['MSFT', '', '51.23']
DEBUG:fileparse:Ligne 4: Raison : valeur littérale invalide pour int() avec base 10 : ''
AVERTISSEMENT:fileparse:Ligne 7: Mauvaise ligne : ['IBM', '', '70.44']
DEBUG:fileparse:Ligne 7: Raison : valeur littérale invalide pour int() avec base 10 : ''
>>>
```

Désactivez tous les messages de journalisation, sauf les plus critiques :

```python
>>> logging.getLogger('fileparse').setLevel(logging.CRITIQUE)
>>> a = report.read_portfolio('missing.csv')
>>>
```
