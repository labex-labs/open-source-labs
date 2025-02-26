# Упражнение 7.8: упрощение вызовов функций

В вышеприведенном примере пользователи могут найти вызовы, такие как `typedproperty('shares', int)`, несколько громоздкими для ввода - особенно если они повторяются часто. Добавьте следующие определения в файл `typedproperty.py`:

```python
String = lambda name: typedproperty(name, str)
Integer = lambda name: typedproperty(name, int)
Float = lambda name: typedproperty(name, float)
```

Теперь перепишите класс `Stock` для использования этих функций вместо этого:

```python
class Stock:
    name = String('name')
    shares = Integer('shares')
    price = Float('price')

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
```

Ах, это немного лучше. Главное, что можно извлечь здесь, - это то, что замыкания и `lambda` часто могут быть использованы для упрощения кода и устранения раздражающего повторения. Это часто хорошо.
