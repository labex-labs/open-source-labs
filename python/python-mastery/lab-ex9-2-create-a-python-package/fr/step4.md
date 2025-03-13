# Mise à jour et test du programme stock.py

Maintenant que nous avons créé notre package et corrigé les imports internes, il est temps de mettre à jour le fichier `stock.py` pour utiliser notre nouvelle structure de package. Un package en Python est un moyen d'organiser des modules liés ensemble. Cela aide à organiser votre base de code et facilite la gestion et la réutilisation du code.

Ouvrez le fichier `stock.py` dans l'éditeur :

```bash
# Click on stock.py in the file explorer or run:
code stock.py
```

Les imports actuels dans `stock.py` sont basés sur l'ancienne structure où tous les fichiers étaient dans le même répertoire. En Python, lorsque vous importez un module, Python recherche le module dans des emplacements spécifiques. Dans l'ancienne structure, puisque tous les fichiers étaient dans le même répertoire, Python pouvait facilement trouver les modules. Mais maintenant, avec la nouvelle structure de package, nous devons mettre à jour les imports pour indiquer à Python où trouver les modules dans le package `structly`.

Mettez à jour le fichier `stock.py` pour qu'il ressemble exactement à ceci :

```python
# stock.py

from structly.structure import Structure, String, PositiveInteger, PositiveFloat

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

Les principales modifications sont les suivantes :

1. Changement de `from structure import Structure, String, PositiveInteger, PositiveFloat` en `from structly.structure import Structure, String, PositiveInteger, PositiveFloat`. Cette modification indique à Python de rechercher le module `structure` à l'intérieur du package `structly`.
2. Changement de `from reader import read_csv_as_instances` en `from structly.reader import read_csv_as_instances`. De même, cette modification dirige Python pour trouver le module `reader` dans le package `structly`.
3. Changement de `from tableformat import create_formatter, print_table` en `from structly.tableformat import create_formatter, print_table`. Cela garantit que Python localise le module `tableformat` dans le package `structly`.

Sauvegardez le fichier après avoir effectué ces modifications. Sauvegarder le fichier est important car cela garantit que les modifications que vous avez apportées sont enregistrées et peuvent être utilisées lorsque vous exécutez le programme.

Maintenant, testons notre code mis à jour pour nous assurer que tout fonctionne correctement :

```bash
python stock.py
```

Vous devriez voir la sortie suivante :

```
      name      shares       price
---------- ---------- ----------
      MSFT        100      51.23
       IBM         50       91.1
      AAPL         75     145.89
      ACME        125     123.45
       HPE         75       32.2
```

Si vous voyez cette sortie, félicitations ! Vous avez créé avec succès un package Python et mis à jour votre code pour l'utiliser. Cela signifie que votre code est maintenant organisé de manière plus modulaire, ce qui le rend plus facile à maintenir et à développer à l'avenir.
