# Création d'un package

Dans les exercices précédents, vous avez créé les fichiers suivants liés à des structures vérifiées au type, à la lecture de données et à la création de tableaux :

- `structure.py`
- `validate.py`
- `reader.py`
- `tableformat.py`

Votre tâche consiste à prendre tous ces fichiers et à les déplacer dans un package appelé `structly`. Pour ce faire, suivez ces étapes :

- Créez un répertoire appelé `structly`
- Créez un fichier vide `__init__.py` et placez-le dans le répertoire `structly`
- Déplacez les fichiers `structure.py`, `validate.py`, `reader.py` et `tableformat.py` dans le répertoire `structly`.
- Corrigez toutes les instructions d'importation entre les modules (en particulier, le module `structure` dépend de `validate`).

Une fois que vous avez fait cela, modifiez le programme `stock.py` de sorte qu'il ait exactement cette apparence et fonctionne :

```python
# stock.py

from structly.structure import Structure

class Stock(Structure):
    name = String()
    shares = PositiveInteger()
    price = PositiveFloat()

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares: PositiveInteger):
        self.shares -= nshares

if __name__ == '__main__':
    from structly.reader import read_csv_as_instances
    from structly.tableformat import create_formatter, print_table
    portfolio = read_csv_as_instances('portfolio.csv', Stock)
    formatter = create_formatter('text')
    print_table(portfolio, ['name','shares','price'], formatter)
```
