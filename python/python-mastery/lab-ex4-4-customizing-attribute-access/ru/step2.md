# Создание объектов только для чтения с использованием прокси

В этом шаге мы рассмотрим прокси - классы, очень полезный паттерн в Python. Прокси - классы позволяют взять существующий объект и изменить его поведение без изменения его исходного кода. Это похоже на то, что вы оборачиваете объект специальной оболочкой, чтобы добавить новые функции или ограничения.

## Что такое прокси?

Прокси - это объект, который находится между вами и другим объектом. Он имеет ту же набор функций и свойств, что и исходный объект, но может выполнять дополнительные действия. Например, он может контролировать, кто может получить доступ к объекту, вести запись действий (логирование) или добавлять другие полезные функции.

Давайте создадим прокси только для чтения. Такой прокси не позволит вам изменять атрибуты объекта.

### Шаг 1: Создание класса прокси только для чтения

Сначала нам нужно создать файл Python, в котором будет определен наш прокси только для чтения.

1. Перейдите в директорию `/home/labex/project`.
2. Создайте новый файл с именем `readonly_proxy.py` в этой директории.
3. Откройте файл `readonly_proxy.py` и добавьте следующий код:

```python
class ReadonlyProxy:
    def __init__(self, obj):
        # Store the wrapped object directly in __dict__ to avoid triggering __setattr__
        self.__dict__['_obj'] = obj

    def __getattr__(self, name):
        # Forward attribute access to the wrapped object
        return getattr(self._obj, name)

    def __setattr__(self, name, value):
        # Block all attribute assignments
        raise AttributeError("Cannot modify a read-only object")
```

В этом коде определен класс `ReadonlyProxy`. Метод `__init__` сохраняет объект, который мы хотим обернуть. Мы используем `self.__dict__` для прямого сохранения объекта, чтобы избежать вызова метода `__setattr__`. Метод `__getattr__` вызывается, когда мы пытаемся получить доступ к атрибуту прокси. Он просто перенаправляет запрос к обернутому объекту. Метод `__setattr__` вызывается, когда мы пытаемся изменить атрибут. Он вызывает ошибку, чтобы предотвратить любые изменения.

### Шаг 2: Создание тестового файла

Теперь мы создадим тестовый файл, чтобы посмотреть, как работает наш прокси только для чтения.

1. Создайте новый файл с именем `test_readonly.py` в той же директории `/home/labex/project`.
2. Добавьте следующий код в файл `test_readonly.py`:

```python
from stock import Stock
from readonly_proxy import ReadonlyProxy

# Create a normal Stock object
stock = Stock('AAPL', 100, 150.75)
print("Original stock object:")
print(f"Name: {stock.name}")
print(f"Shares: {stock.shares}")
print(f"Price: {stock.price}")
print(f"Cost: {stock.cost}")

# Modify the original stock object
stock.shares = 200
print(f"\nAfter modification - Shares: {stock.shares}")
print(f"After modification - Cost: {stock.cost}")

# Create a read-only proxy around the stock
readonly_stock = ReadonlyProxy(stock)
print("\nRead-only proxy object:")
print(f"Name: {readonly_stock.name}")
print(f"Shares: {readonly_stock.shares}")
print(f"Price: {readonly_stock.price}")
print(f"Cost: {readonly_stock.cost}")

# Try to modify the read-only proxy
try:
    print("\nAttempting to modify the read-only proxy...")
    readonly_stock.shares = 300
except AttributeError as e:
    print(f"Error: {e}")

# Show that the original object is unchanged
print(f"\nOriginal stock shares are still: {stock.shares}")
```

В этом тестовом коде мы сначала создаем обычный объект `Stock` и выводим его информацию. Затем мы изменяем один из его атрибутов и выводим обновленную информацию. Далее мы создаем прокси только для чтения для объекта `Stock` и выводим его информацию. Наконец, мы пытаемся изменить прокси только для чтения и ожидаем получить ошибку.

### Шаг 3: Запуск тестового скрипта

После создания класса прокси и тестового файла нам нужно запустить тестовый скрипт, чтобы увидеть результаты.

1. Откройте терминал и перейдите в директорию `/home/labex/project` с помощью следующей команды:

```bash
cd /home/labex/project
```

2. Запустите тестовый скрипт с помощью следующей команды:

```bash
python3 test_readonly.py
```

Вы должны увидеть вывод, похожий на следующий:

```
Original stock object:
Name: AAPL
Shares: 100
Price: 150.75
Cost: 15075.0

After modification - Shares: 200
After modification - Cost: 30150.0

Read-only proxy object:
Name: AAPL
Shares: 200
Price: 150.75
Cost: 30150.0

Attempting to modify the read-only proxy...
Error: Cannot modify a read-only object

Original stock shares are still: 200
```

## Как работает прокси

Класс `ReadonlyProxy` использует два специальных метода, чтобы обеспечить функциональность только для чтения:

1. `__getattr__(self, name)`: Этот метод вызывается, когда Python не может найти атрибут обычным способом. В нашем классе `ReadonlyProxy` мы используем функцию `getattr()`, чтобы перенаправить запрос на доступ к атрибуту к обернутому объекту. Таким образом, когда вы пытаетесь получить доступ к атрибуту прокси, он на самом деле получит атрибут из обернутого объекта.

2. `__setattr__(self, name, value)`: Этот метод вызывается, когда вы пытаетесь присвоить значение атрибуту. В нашей реализации мы вызываем исключение `AttributeError`, чтобы предотвратить любые изменения атрибутов прокси.

3. В методе `__init__` мы напрямую изменяем `self.__dict__`, чтобы сохранить обернутый объект. Это важно, потому что если бы мы использовали обычный способ присвоения объекта, он бы вызвал метод `__setattr__`, который бы вызвал ошибку.

Этот паттерн прокси позволяет нам добавить слой только для чтения вокруг любого существующего объекта без изменения его исходного класса. Прокси - объект ведет себя так же, как и обернутый объект, но не позволит вам внести какие - либо изменения.
