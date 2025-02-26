# Evaluation différée

Considérez une fonction comme celle-ci :

```python
def after(seconds, func):
    import time
    time.sleep(seconds)
    func()
```

Exemple d'utilisation :

```python
def greeting():
    print('Hello Guido')

after(30, greeting)
```

`after` exécute la fonction fournie... plus tard.

Les closures transportent des informations supplémentaires.

```python
def add(x, y):
    def do_add():
        print(f'Adding {x} + {y} -> {x+y}')
    return do_add

def after(seconds, func):
    import time
    time.sleep(seconds)
    func()

after(30, add(2, 3))
# `do_add` a les références x -> 2 et y -> 3
```
