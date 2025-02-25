# Exercice 1.33 : Lecture à partir de la ligne de commande

Dans le programme `pcost.py`, le nom du fichier d'entrée a été codé en dur dans le code :

```python
# pcost.py

def portfolio_cost(filename):
  ...
    # Votre code ici
  ...

cost = portfolio_cost('portfolio.csv')
print('Coût total :', cost)
```

Cela est bien pour l'apprentissage et les tests, mais dans un programme réel, vous ne feriez probablement pas cela.

Au lieu de cela, vous pourriez passer le nom du fichier en tant qu'argument à un script. Essayez de modifier la partie inférieure du programme comme suit :

```python
# pcost_1.33.py

import csv


def portfolio_cost(filename):
    """
    Calcule le coût total (nombre d'actions * prix) d'un fichier de portefeuille
    """
    total_cost = 0.0

    with open(filename, "rt") as f:
        rows = csv.reader(f)
        headers = next(rows)  # Passez à la ligne d'en-tête
        for row in rows:
            if len(row) < 3:
                print("Ignorer la ligne invalide :", row)
                continue
            try:
                nshares = int(row[1])
                price = float(row[2])
                total_cost += nshares * price
            except (IndexError, ValueError):
                print("Ignorer la ligne invalide :", row)

    return total_cost

import sys


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'portfolio.csv'

cost = portfolio_cost(filename)
print('Coût total :', cost)
```

`sys.argv` est une liste qui contient les arguments passés sur la ligne de commande (s'il y en a).

Pour exécuter votre programme, vous devrez exécuter Python à partir du terminal.

Par exemple, à partir de bash sur Unix :

```bash
$ python3 pcost.py portfolio.csv
Coût total : 44671.15
bash %
```
