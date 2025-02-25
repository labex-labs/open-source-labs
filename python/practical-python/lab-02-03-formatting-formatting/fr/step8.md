# Exercice 2.10 : Affichage d'un tableau formaté

Refaites la boucle `for` de l'exercice 2.9, mais changez l'instruction `print` pour formater les tuples.

```python
>>> for r in rapport:
        print('%10s %10d %10.2f %10.2f' % r)

          AA        100       9,22     -22,98
         IBM         50     106,28      15,18
         CAT        150      35,46     -47,98
        MSFT        200      20,89     -30,34
...
>>>
```

Vous pouvez également étendre les valeurs et utiliser les `f-strings`. Par exemple :

```python
>>> for nom, actions, prix, changement in rapport:
        print(f'{nom:>10s} {actions:>10d} {prix:>10.2f} {changement:>10.2f}')

          AA        100       9,22     -22,98
         IBM         50     106,28      15,18
         CAT        150      35,46     -47,98
        MSFT        200      20,89     -30,34
...
>>>
```

Prenez les instructions ci-dessus et ajoutez-les à votre programme `report.py`. Faites en sorte que votre programme prenne la sortie de la fonction `make_report()` et affiche un tableau correctement formaté comme indiqué.
