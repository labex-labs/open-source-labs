# Exercice 6.4 : Un générateur simple

Si vous vous trouvez à avoir besoin de personnaliser une itération, vous devriez toujours penser aux fonctions génératrices. Elles sont faciles à écrire - créez une fonction qui exécute la logique d'itération souhaitée et utilisez `yield` pour émettre des valeurs.

Par exemple, essayez ce générateur qui recherche dans un fichier les lignes contenant une sous-chaîne correspondante :

```python
>>> def filematch(filename, substr):
        with open(filename, 'r') as f:
            for line in f:
                if substr in line:
                    yield line

>>> for line in open('portfolio.csv'):
        print(line, end='')

name,shares,price
"AA",100,32.20
"IBM",50,91.10
"CAT",150,83.44
"MSFT",200,51.23
"GE",95,40.37
"MSFT",50,65.10
"IBM",100,70.44
>>> for line in filematch('portfolio.csv', 'IBM'):
        print(line, end='')

"IBM",50,91.10
"IBM",100,70.44
>>>
```

C'est assez intéressant - l'idée que vous pouvez cacher un certain traitement personnalisé dans une fonction et l'utiliser pour alimenter une boucle `for`. L'exemple suivant examine un cas plus inhabituel.
