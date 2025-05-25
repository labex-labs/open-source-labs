# Avaliação Atrasada (Delayed Evaluation)

Considere uma função como esta:

```python
def after(seconds, func):
    import time
    time.sleep(seconds)
    func()
```

Exemplo de uso:

```python
def greeting():
    print('Hello Guido')

after(30, greeting)
```

`after` executa a função fornecida... mais tarde.

Closures (fechamentos) carregam informações extras.

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
# `do_add` has the references x -> 2 and y -> 3
```
