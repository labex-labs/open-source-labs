# Exercice 3.15 : Fonctions `main()`

Dans le fichier `report.py`, ajoutez une fonction `main()` qui accepte une liste d'options de ligne de commande et produit la même sortie que précédemment. Vous devriez être capable de l'exécuter de manière interactive comme ceci :

```python
>>> import report
>>> report.main(['/home/labex/project/report.py', '/home/labex/project/portfolio.csv', '/home/labex/project/prices.csv'])
      Name     Shares      Price     Change
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

Modifiez le fichier `pcost.py` de manière à ce qu'il ait une fonction `main()` similaire :

```python
>>> import pcost
>>> pcost.main(['/home/labex/project/pcost.py', '/home/labex/project/portfolio.csv'])
Total cost: 44671.15
>>>
```
