# Votre premier décorateur

Pour commencer avec les décorateurs, écrivez une fonction décoratrice _très_ simple qui n'affiche qu'un message chaque fois qu'une fonction est appelée. Créez un fichier `logcall.py` et définissez la fonction suivante :

```python
# logcall.py

def logged(func):
    print('Adding logging to', func.__name__)
    def wrapper(*args, **kwargs):
        print('Calling', func.__name__)
        return func(*args, **kwargs)
    return wrapper
```

Maintenant, créez un fichier séparé `sample.py` et appliquez-le à quelques définitions de fonction :

```python
# sample.py

from logcall import logged

@logged
def add(x,y):
    return x+y

@logged
def sub(x,y):
    return x-y
```

Testez votre code comme suit :

```python
>>> import sample
Adding logging to add
Adding logging to sub
>>> sample.add(3,4)
Calling add
7
>>> sample.sub(2,3)
Calling sub
-1
>>>
```
