# Découpage des modules

Le fichier `structly/tableformat.py` contient le code pour créer des tableaux dans différents formats. Plus précisément :

- Une classe de base `TableFormatter`.
- Une classe `TextTableFormatter`.
- Une classe `CSVTableFormatter`.
- Une classe `HTMLTableFormatter`.

Au lieu d'avoir toutes ces classes dans un seul fichier `.py`, peut-être serait-il plus logique de déplacer chaque formatteur concret dans son propre fichier. Pour ce faire, nous allons diviser le fichier `tableformat.py` en parties. Suivez attentivement les instructions suivantes :

Tout d'abord, supprimez le répertoire `structly/__pycache__`.

    % cd structly
    % rm -rf __pycache__

Ensuite, créez le répertoire `structly/tableformat`. Ce répertoire doit avoir exactement le même nom que le module qu'il remplace (`tableformat.py`).

```bash
mkdir tableformat
```

Déplacez le fichier `tableformat.py` original dans le nouveau répertoire `tableformat` et renommez-le en `formatter.py`.

```bash
mv tableformat.py tableformat/formatter.py
```

Dans le répertoire `tableformat`, divisez le code de `tableformat.py` dans les fichiers et répertoires suivants :

- `formatter.py` - Contient la classe de base `TableFormatter`, les mixins et diverses fonctions.
- `formats/text.py` - Contient la classe `TextTableFormatter`.
- `formats/csv.py` - Contient la classe `CSVTableFormatter`.
- `formats/html.py` - Contient la classe `HTMLTableFormatter`.

Ajoutez un fichier `__init__.py` dans les répertoires `tableformat/` et `tableformat/formats`. Que le fichier `tableformat/__init__.py` exporte les mêmes symboles que le fichier `tableformat.py` original.

Après avoir effectué tous ces changements, vous devriez avoir une structure de package qui ressemble à ceci :

    structly/
          __init__.py
          validate.py
          reader.py
          structure.py
          tableformat/
               __init__.py
               formatter.py
               formats/
                   __init__.py
                   text.py
                   csv.py
                   html.py

Pour les utilisateurs, tout devrait fonctionner exactement comme avant. Par exemple, votre fichier `stock.py` précédent devrait fonctionner :

```python
# stock.py

from structly import *

class Stock(Structure):
    name = String()
    shares = PositiveInteger()
    price = PositiveFloat()

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares

if __name__ == '__main__':
    portfolio = read_csv_as_instances('portfolio.csv', Stock)
    formatter = create_formatter('text')
    print_table(portfolio, ['name','shares','price'], formatter)
```
