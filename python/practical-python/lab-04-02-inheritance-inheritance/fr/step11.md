# Héritage multiple

Vous pouvez hériter de plusieurs classes en les spécifiant dans la définition de la classe.

```python
class Mother:
...

class Father:
...

class Child(Mother, Father):
...
```

La classe `Child` hérite des caractéristiques des deux parents. Il y a quelques détails assez complexes. Ne le faites pas à moins de savoir ce que vous faites. Plus d'informations seront données dans la section suivante, mais nous n'allons pas utiliser l'héritage multiple plus loin dans ce cours.

Un usage majeur de l'héritage est d'écrire du code conçu pour être étendu ou personnalisé de diverses manières - en particulier dans des bibliothèques ou des frameworks. Pour illustrer, considérez la fonction `print_report()` dans votre programme `report.py`. Elle devrait ressembler à ceci :

```python
def print_report(reportdata):
    '''
    Affiche un tableau bien formaté à partir d'une liste de tuples (nom, actions, prix, variation).
    '''
    headers = ('Nom','Actions','Prix','Variation')
    print('%10s %10s %10s %10s' % headers)
    print(('-'*10 +' ')*len(headers))
    for row in reportdata:
        print('%10s %10d %10.2f %10.2f' % row)
```

Lorsque vous exécutez votre programme de rapport, vous devriez obtenir une sortie comme celle-ci :

```python
>>> import report
>>> report.portfolio_report('portfolio.csv', 'prices.csv')
      Nom     Actions      Prix     Variation
---------- ---------- ---------- ----------
        AA        100       9.22     -22.98
       IBM         50     106.28      15.18
       CAT        150      35.46     -47.98
      MSFT        200      20.89     -30.34
        GE         95      13.48     -26.89
      MSFT         50      20.89     -44.21
       IBM        100     106.28      35.84
```
