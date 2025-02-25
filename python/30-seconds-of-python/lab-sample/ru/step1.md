# Случайный элемент в списке

Напишите функцию `random_element(lst)`, которая принимает список в качестве аргумента и возвращает случайный элемент из этого списка.

- Используйте `random.choice()`, чтобы получить случайный элемент из `lst`.

```python
from random import choice

def sample(lst):
  return choice(lst)
```

```python
sample([3, 7, 9, 11]) # 9
```
