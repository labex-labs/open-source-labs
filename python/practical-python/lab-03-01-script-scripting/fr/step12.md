# Exercice 3.2 : Création d'une fonction de niveau supérieur pour l'exécution du programme

Prenez la dernière partie de votre programme et empaquetez-la dans une fonction unique `portfolio_report(portfolio_filename, prices_filename)`. Faites en sorte que la fonction fonctionne de telle manière que l'appel de fonction suivant crée le rapport comme auparavant :

```python
portfolio_report('/home/labex/project/portfolio.csv', '/home/labex/project/prices.csv')
```

Dans cette version finale, votre programme ne sera rien de plus qu'une série de définitions de fonctions suivies d'un seul appel de fonction à `portfolio_report()` à la toute fin (qui exécute toutes les étapes impliquées dans le programme).

En transformant votre programme en une seule fonction, il devient facile de l'exécuter avec différents entrées. Par exemple, essayez ces instructions de manière interactive après avoir exécuté votre programme :

```python
>>> portfolio_report('/home/labex/project/portfolio2.csv', '/home/labex/project/prices.csv')
... regardez la sortie...
>>> files = ['/home/labex/project/portfolio.csv', '/home/labex/project/portfolio2.csv']
>>> for name in files:
        print(f'{name:-^43s}')
        portfolio_report(name, '/home/labex/project/prices.csv')
        print()

... regardez la sortie...
>>>
```
