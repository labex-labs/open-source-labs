# Exercice 4.4 : Utilisation de votre classe

Modifiez la fonction `read_portfolio()` dans le programme `report.py` de sorte qu'elle lise un portefeuille dans une liste d'instances de `Stock` comme indiqué dans l'Exercice 4.3. Une fois que vous avez fait cela, corrigez tout le code dans `report.py` et `pcost.py` de sorte qu'il fonctionne avec des instances de `Stock` au lieu de dictionnaires.

Indice : Vous n'avez pas besoin d'apporter de grandes modifications au code. Vous devriez principalement changer l'accès au dictionnaire tel que `s['shares']` en `s.shares`.

Vous devriez être capable d'exécuter vos fonctions comme avant :

```python
>>> import pcost
>>> pcost.portfolio_cost('portfolio.csv')
44671.15
>>> import report
>>> report.portfolio_report('portfolio.csv', 'prices.csv')
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
