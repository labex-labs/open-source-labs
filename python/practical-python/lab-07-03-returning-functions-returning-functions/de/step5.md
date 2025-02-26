# Verzögerte Auswertung

Betrachten Sie eine Funktion wie diese:

```python
def after(seconds, func):
    import time
    time.sleep(seconds)
    func()
```

Verwendungsbeispiel:

```python
def greeting():
    print('Hello Guido')

after(30, greeting)
```

`after` führt die bereitgestellte Funktion... später aus.

Closures tragen zusätzliche Informationen mit sich.

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
# `do_add` hat die Referenzen x -> 2 und y -> 3
```
