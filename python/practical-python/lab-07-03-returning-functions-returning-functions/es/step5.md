# Evaluación diferida

Considere una función como esta:

```python
def after(seconds, func):
    import time
    time.sleep(seconds)
    func()
```

Ejemplo de uso:

```python
def greeting():
    print('Hello Guido')

after(30, greeting)
```

`after` ejecuta la función suministrada... más tarde.

Las cerraduras llevan información adicional.

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
# `do_add` tiene las referencias x -> 2 e y -> 3
```
