# Lecture d'un portefeuille

Ajoutez une fonction `read_portfolio()` à votre programme `stock.py` qui lit un fichier de données de portefeuille dans une liste d'objets `Stock`. Voici comment elle devrait fonctionner :

```python
>>> portfolio = read_portfolio('portfolio.csv')
>>> for s in portfolio:
        print(s)

<__main__.Stock object at 0x3902f0>
<__main__.Stock object at 0x390270>
<__main__.Stock object at 0x390330>
<__main__.Stock object at 0x390370>
<__main__.Stock object at 0x3903b0>
<__main__.Stock object at 0x3903f0>
<__main__.Stock object at 0x390430>
>>>
```

Vous avez déjà écrit une fonction similaire dans le cadre de l'exercice 2.3. Discussion sur la conception : `read_portfolio()` devrait-elle être une fonction séparée ou une partie de la définition de la classe?

## Note :

Ajoutez la fonction `read_portfolio()` dans le fichier `stock.py`.
