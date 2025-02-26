# Classes de modèle d'algorithme

Le fichier `reader.py` contient deux fonctions, `read_csv_as_dicts()` et `read_csv_as_instances()`. Les deux fonctions sont presque identiques - il n'y a qu'un tout petit bout de code qui est différent. Peut-être que ce code pourrait être consolidé en une définition de classe de quelque sorte. Ajoutez la classe suivante au fichier `reader.py` :

```python
# reader.py


import csv
from abc import ABC, abstractmethod

class CSVParser(ABC):

    def parse(self, filename):
        records = []
        with open(filename) as f:
            rows = csv.reader(f)
            headers = next(rows)
            for row in rows:
                record = self.make_record(headers, row)
                records.append(record)
        return records

    @abstractmethod
    def make_record(self, headers, row):
        pass
```

Ce code fournit une structure (ou un modèle) de la fonctionnalité d'analyse de CSV. Pour l'utiliser, vous en créez une sous-classe, ajoutez tout attribut supplémentaire dont vous pourriez avoir besoin et redéfinissez la méthode `make_record()`. Par exemple :

```python
class DictCSVParser(CSVParser):
    def __init__(self, types):
        self.types = types

    def make_record(self, headers, row):
        return { name: func(val) for name, func, val in zip(headers, self.types, row) }

class InstanceCSVParser(CSVParser):
    def __init__(self, cls):
        self.cls = cls

    def make_record(self, headers, row):
        return self.cls.from_row(row)
```

Ajoutez les classes ci-dessus au fichier `reader.py`. Voici comment vous utiliseriez l'une d'entre elles :

```python
>>> from reader import DictCSVParser
>>> parser = DictCSVParser([str, int, float])
>>> port = parser.parse('portfolio.csv')
>>>
```

Ça fonctionne, mais c'est un peu gênant. Pour corriger cela, réimplémentez les fonctions `read_csv_as_dicts()` et `read_csv_as_instances()` pour utiliser ces classes. Votre code refactorisé devrait fonctionner exactement de la même manière que précédemment. Par exemple :

```python
>>> import reader
>>> import stock
>>> port = reader.read_csv_as_instances('portfolio.csv', stock.Stock)
>>>
```
