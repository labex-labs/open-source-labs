# Понимание метода `__setattr__` для управления атрибутами

В Python есть специальные методы, которые позволяют настраивать, как к атрибутам объекта осуществляется доступ и как они изменяются. Одним из таких важных методов является `__setattr__()`. Этот метод вызывается каждый раз, когда вы пытаетесь присвоить значение атрибуту объекта. Он позволяет вам тонко управлять процессом присвоения атрибутов.

## Что такое `__setattr__`?

Метод `__setattr__(self, name, value)` действует как перехватчик для всех операций присвоения атрибутов. Когда вы пишете простой оператор присваивания, например `obj.attr = value`, Python не просто напрямую присваивает значение. Вместо этого он внутренне вызывает `obj.__setattr__("attr", value)`. Эта механика позволяет вам решить, что должно происходить во время присвоения атрибута.

Теперь давайте рассмотрим практический пример того, как можно использовать `__setattr__` для ограничения того, какие атрибуты можно устанавливать в классе.

### Шаг 1: Создание нового файла

Сначала откройте новый файл в WebIDE. Вы можете сделать это, кликнув на меню "File" и выбрав "New File". Назовите этот файл `restricted_stock.py` и сохраните его в директории `/home/labex/project`. В этом файле будет определен класс, в котором мы будем использовать `__setattr__` для управления присвоением атрибутов.

### Шаг 2: Добавление кода в `restricted_stock.py`

Добавьте следующий код в файл `restricted_stock.py`. Этот код определяет класс `RestrictedStock`.

```python
class RestrictedStock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def __setattr__(self, name, value):
        # Only allow specific attributes
        if name not in {'name', 'shares', 'price'}:
            raise AttributeError(f'Cannot set attribute {name}')

        # If attribute is allowed, set it using the parent method
        super().__setattr__(name, value)
```

В методе `__init__` мы инициализируем объект атрибутами `name`, `shares` и `price`. Метод `__setattr__` проверяет, находится ли имя атрибута, которое мы пытаемся присвоить, в наборе разрешенных атрибутов (`name`, `shares`, `price`). Если оно не находится, он вызывает исключение `AttributeError`. Если атрибут разрешен, он использует метод `__setattr__` родительского класса для фактического присвоения атрибута.

### Шаг 3: Создание тестового файла

Создайте новый файл с именем `test_restricted.py` и добавьте в него следующий код. Этот код будет тестировать функциональность класса `RestrictedStock`.

```python
from restricted_stock import RestrictedStock

# Create a new stock
stock = RestrictedStock('GOOG', 100, 490.1)

# Test accessing existing attributes
print(f"Name: {stock.name}")
print(f"Shares: {stock.shares}")
print(f"Price: {stock.price}")

# Test modifying an existing attribute
print("\nChanging shares to 75...")
stock.shares = 75
print(f"New shares value: {stock.shares}")

# Test setting an invalid attribute
try:
    print("\nTrying to set an invalid attribute 'share'...")
    stock.share = 50
except AttributeError as e:
    print(f"Error: {e}")
```

В этом коде мы сначала импортируем класс `RestrictedStock`. Затем создаем экземпляр этого класса. Мы тестируем доступ к существующим атрибутам, изменение существующего атрибута и, наконец, пытаемся установить недопустимый атрибут, чтобы проверить, работает ли метод `__setattr__` как ожидается.

### Шаг 4: Запуск тестового файла

Откройте терминал в WebIDE и выполните следующие команды для запуска файла `test_restricted.py`:

```bash
cd /home/labex/project
python3 test_restricted.py
```

После выполнения этих команд вы должны увидеть вывод, похожий на следующий:

```
Name: GOOG
Shares: 100
Price: 490.1

Changing shares to 75...
New shares value: 75

Trying to set an invalid attribute 'share'...
Error: Cannot set attribute share
```

## Как это работает

Метод `__setattr__` в нашем классе `RestrictedStock` работает в следующих шагах:

1. Сначала он проверяет, находится ли имя атрибута в наборе разрешенных (`name`, `shares`, `price`).
2. Если имя атрибута не находится в наборе разрешенных, он вызывает исключение `AttributeError`. Это предотвращает присвоение нежелательных атрибутов.
3. Если атрибут разрешен, он использует `super().__setattr__()` для фактического присвоения атрибута. Это гарантирует, что для разрешенных атрибутов происходит обычный процесс присвоения атрибутов.

Этот метод более гибок, чем использование `__slots__`, которое мы видели в предыдущих примерах. В то время как `__slots__` может оптимизировать использование памяти и ограничить атрибуты, у него есть ограничения при работе с наследованием и он может конфликтовать с другими функциями Python. Наш подход с использованием `__setattr__` дает нам аналогичный контроль над присвоением атрибутов без некоторых из этих ограничений.
