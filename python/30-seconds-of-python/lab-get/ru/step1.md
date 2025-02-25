# Получить вложенное значение

Напишите функцию `get(d, selectors)`, которая принимает в качестве аргументов словарь или список `d` и список селекторов `selectors` и возвращает значение вложенного ключа, указанного заданным списком селекторов. Если ключ не существует, верните `None`.

Для реализации этой функции используйте `functools.reduce()`, чтобы пройти по списку `selectors`. Примените `operator.getitem()` для каждого ключа в `selectors`, получая значение, которое будет использоваться в качестве элемента для следующей итерации.

```python
from functools import reduce
from operator import getitem

def get(d, selectors):
  return reduce(getitem, selectors, d)
```

```python
users = {
  'freddy': {
    'name': {
      'first': 'fred',
      'last': 'smith'
    },
    'postIds': [1, 2, 3]
  }
}
get(users, ['freddy', 'name', 'last']) # 'smith'
get(users, ['freddy', 'postIds', 1]) # 2
```
