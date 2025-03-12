# Tester notre implémentation

Maintenant que nous avons implémenté notre métaclasse et modifié la classe `Structure`, il est temps de tester notre implémentation. Le test est crucial car il nous aide à nous assurer que tout fonctionne correctement. En exécutant des tests, nous pouvons détecter tout problème potentiel dès le départ et nous assurer que notre code se comporte comme prévu.

Tout d'abord, exécutons les tests unitaires pour voir si notre classe `Stock` fonctionne comme prévu. Les tests unitaires sont de petits tests isolés qui vérifient les parties individuelles de notre code. Dans ce cas, nous voulons nous assurer que la classe `Stock` fonctionne correctement. Pour exécuter les tests unitaires, nous utiliserons la commande suivante dans le terminal :

```bash
python3 teststock.py
```

Si tout fonctionne correctement, tous les tests devraient passer sans erreur. Lorsque les tests sont exécutés avec succès, la sortie devrait ressembler à ceci :

```
........
----------------------------------------------------------------------
Ran 6 tests in 0.001s

OK
```

Les points représentent chaque test qui a réussi, et le `OK` final indique que tous les tests ont été un succès.

Maintenant, testons notre classe `Stock` avec des données réelles et la fonctionnalité de formatage de table. Cela nous donnera un scénario plus réaliste pour voir comment notre classe `Stock` interagit avec les données et comment le formatage de table fonctionne. Nous utiliserons la commande suivante dans le terminal :

```bash
python3 -c "
from stock import Stock
from reader import read_csv_as_instances
from tableformat import create_formatter, print_table

# Read portfolio data into Stock instances
portfolio = read_csv_as_instances('portfolio.csv', Stock)
print('Portfolio:')
print(portfolio)

# Format and print the portfolio data
print('\nFormatted table:')
formatter = create_formatter('text')
print_table(portfolio, ['name', 'shares', 'price'], formatter)
"
```

Dans ce code, nous importons d'abord les classes et les fonctions nécessaires. Ensuite, nous lisons les données d'un fichier CSV dans des instances de `Stock`. Après cela, nous affichons les données du portefeuille, puis nous les formatons en tableau et affichons le tableau formaté.

Vous devriez voir une sortie similaire à celle - ci :

```
Portfolio:
[Stock('AA',100,32.2), Stock('IBM',50,91.1), Stock('CAT',150,83.44), Stock('MSFT',200,51.23), Stock('GE',95,40.37), Stock('MSFT',50,65.1), Stock('IBM',100,70.44)]

Formatted table:
      name     shares      price
---------- ---------- ----------
        AA        100       32.2
       IBM         50       91.1
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50       65.1
       IBM        100      70.44
```

Prenez un moment pour apprécier ce que nous avons accompli :

1. Nous avons créé un mécanisme pour collecter automatiquement tous les types de validateurs. Cela signifie que nous n'avons pas à suivre manuellement tous les validateurs, ce qui nous fait gagner du temps et réduit le risque d'erreurs.
2. Nous avons implémenté une métaclasse qui injecte ces types dans l'espace de noms des sous - classes de `Structure`. Cela permet aux sous - classes d'utiliser ces validateurs sans avoir à les importer explicitement.
3. Nous avons éliminé le besoin d'importations explicites des types de validateurs. Cela rend notre code plus propre et plus facile à lire.
4. Tout cela se passe en coulisse, ce qui rend le code pour définir de nouvelles structures propre et simple.

Le fichier final `stock.py` est remarquablement propre par rapport à ce qu'il aurait été sans notre métaclasse :

```python
from structure import Structure

class Stock(Structure):
    name = String()
    shares = PositiveInteger()
    price = PositiveFloat()

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares: PositiveInteger):
        self.shares -= nshares
```

Sans avoir besoin d'importer directement les types de validateurs, le code est plus concis et plus facile à maintenir. Ceci est un excellent exemple de la façon dont les métaclasses peuvent améliorer la qualité de notre code.
