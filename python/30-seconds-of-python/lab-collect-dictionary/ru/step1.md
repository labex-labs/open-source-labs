# Инвертировать словарь

Напишите функцию `invert_dictionary(obj)`, которая принимает на вход словарь `obj` и возвращает новый словарь с инвертированными ключами и значениями. Входной словарь будет иметь неуникальные хэшируемые значения. Если два или более ключей имеют одно и то же значение, функция должна добавить ключи в список в выходном словаре.

Для решения этой проблемы вы можете следовать следующим шагам:

1. Создайте `collections.defaultdict` с `list` в качестве значения по умолчанию для каждого ключа.
2. Используйте `dictionary.items()` в сочетании с циклом, чтобы сопоставить значения словаря с ключами с использованием `dict.append()`.
3. Используйте `dict()` для преобразования `collections.defaultdict` в обычный словарь.

Подпись функции: `def invert_dictionary(obj: dict) -> dict:`

```python
from collections import defaultdict

def collect_dictionary(obj):
  inv_obj = defaultdict(list)
  for key, value in obj.items():
    inv_obj[value].append(key)
  return dict(inv_obj)
```

```python
ages = {
  'Peter': 10,
  'Isabel': 10,
  'Anna': 9,
}
collect_dictionary(ages) # { 10: ['Peter', 'Isabel'], 9: ['Anna'] }
```
