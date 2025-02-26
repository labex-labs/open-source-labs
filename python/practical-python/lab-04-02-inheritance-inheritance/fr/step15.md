# Exercice 4.8 : Mettre tout ça ensemble

Modifiez le programme `report.py` de sorte que la fonction `portfolio_report()` prenne un argument optionnel spécifiant le format de sortie. Par exemple :

```python
>>> report.portfolio_report('portfolio.csv', 'prices.csv', 'txt')
      Nom     Actions      Prix     Variation
---------- ---------- ---------- ----------
        AA        100       9.22     -22.98
       IBM         50     106.28      15.18
       CAT        150      35.46     -47.98
      MSFT        200      20.89     -30.34
        GE         95      13.48     -26.89
      MSFT         50      20.89     -44.21
       IBM        100     106.28      35.84
>>>
```

Modifiez le programme principal de sorte qu'un format puisse être spécifié sur la ligne de commande :

```bash
$ python3 report.py portfolio.csv prices.csv csv
Nom,Actions,Prix,Variation
AA,100,9.22,-22.98
IBM,50,106.28,15.18
CAT,150,35.46,-47.98
MSFT,200,20.89,-30.34
GE,95,13.48,-26.89
MSFT,50,20.89,-44.21
IBM,100,106.28,35.84
$
```
