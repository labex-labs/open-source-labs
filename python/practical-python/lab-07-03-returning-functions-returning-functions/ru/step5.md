# Отложенная оценка (Delayed Evaluation)

Рассмотрим функцию такого вида:

```python
def after(seconds, func):
    import time
    time.sleep(seconds)
    func()
```

Пример использования:

```python
def greeting():
    print('Hello Guido')

after(30, greeting)
```

`after` выполняет переданную функцию... позже.

Замыкания несут дополнительную информацию.

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
# `do_add` имеет ссылки x -> 2 и y -> 3
```
