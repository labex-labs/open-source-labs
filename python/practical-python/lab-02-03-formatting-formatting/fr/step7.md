# Exercice 2.9 : Collecte de données

Dans l'exercice 2.7, vous avez écrit un programme appelé `report.py` qui calculait le gain/perte d'un portefeuille d'actions. Dans cet exercice, vous allez commencer à le modifier pour produire un tableau comme celui-ci :

          Nom     Actions      Prix     Changement
    ---------- ---------- ---------- ----------
            AA        100       9,22     -22,98
           IBM         50     106,28      15,18
           CAT        150      35,46     -47,98
          MSFT        200      20,89     -30,34
            GE         95      13,48     -26,89
          MSFT         50      20,89     -44,21
           IBM        100     106,28      35,84

Dans ce rapport, "Prix" est le prix actuel d'une action et "Changement" est le changement du prix d'achat initial de l'action.

Pour générer le rapport ci-dessus, vous devrez tout d'abord collecter toutes les données affichées dans le tableau. Écrivez une fonction `make_report()` qui prend une liste d'actions et un dictionnaire de prix en entrée et renvoie une liste de tuples contenant les lignes du tableau ci-dessus.

Ajoutez cette fonction à votre fichier `report.py`. Voici comment cela devrait fonctionner si vous l'essayez en interaction :

```python
>>> portefeuille = read_portfolio('/home/labex/project/portfolio.csv')
>>> prix = read_prices('/home/labex/project/prices.csv')
>>> rapport = make_report(portefeuille, prix)
>>> for r in rapport:
        print(r)

('AA', 100, 9,22, -22,980000000000004)
('IBM', 50, 106,28, 15,180000000000007)
('CAT', 150, 35,46, -47,98)
('MSFT', 200, 20,89, -30,339999999999996)
('GE', 95, 13,48, -26,889999999999997)
...
>>>
```
