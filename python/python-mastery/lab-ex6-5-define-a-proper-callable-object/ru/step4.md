# Вызов: Использование вызываемого объекта в качестве метода

В Python, когда вы используете вызываемый объект в качестве метода внутри класса, возникает особая проблема, которую нужно решить. Вызываемый объект - это то, что можно "вызвать" как функцию, например, сама функция или объект с методом `__call__`. Когда он используется как метод класса, он не всегда работает так, как ожидается, из-за того, как Python передает экземпляр (`self`) в качестве первого аргумента.

Давайте исследуем эту проблему, создав класс `Stock`. Этот класс будет представлять акцию с такими атрибутами, как название, количество акций и цена. Мы также будем использовать валидатор, чтобы убедиться, что данные, с которыми мы работаем, корректны.

Сначала откройте файл `stock.py`, чтобы начать писать наш класс `Stock`. Вы можете использовать следующую команду, чтобы открыть файл в редакторе:

```bash
code /home/labex/project/stock.py
```

Теперь добавьте следующий код в файл `stock.py`. Этот код определяет класс `Stock` с методом `__init__` для инициализации атрибутов акции, свойством `cost` для вычисления общей стоимости и методом `sell` для уменьшения количества акций. Мы также попытаемся использовать `ValidatedFunction` для валидации входных данных для метода `sell`.

```python
from validate import ValidatedFunction, Integer

class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares: Integer):
        self.shares -= nshares

    # Try to use ValidatedFunction
    sell = ValidatedFunction(sell)
```

После определения класса `Stock` нам нужно протестировать его, чтобы убедиться, что он работает как ожидается. Создайте тестовый файл с именем `test_stock.py` и откройте его с помощью следующей команды:

```bash
code /home/labex/project/test_stock.py
```

Добавьте следующий код в файл `test_stock.py`. Этот код создает экземпляр класса `Stock`, выводит начальное количество акций и стоимость, пытается продать некоторые акции, а затем выводит обновленное количество акций и стоимость.

```python
from stock import Stock

try:
    # Create a stock
    s = Stock('GOOG', 100, 490.1)

    # Get the initial cost
    print(f"Initial shares: {s.shares}")
    print(f"Initial cost: ${s.cost}")

    # Try to sell some shares
    s.sell(10)

    # Check the updated cost
    print(f"After selling, shares: {s.shares}")
    print(f"After selling, cost: ${s.cost}")

except Exception as e:
    print(f"Error: {e}")
```

Теперь запустите тестовый файл с помощью следующей команды:

```bash
python3 /home/labex/project/test_stock.py
```

Вероятно, вы столкнетесь с ошибкой, похожей на следующую:

```
Error: missing a required argument: 'nshares'
```

Эта ошибка возникает потому, что когда Python вызывает метод, такой как `s.sell(10)`, на самом деле он вызывает `Stock.sell(s, 10)` в фоновом режиме. Параметр `self` представляет экземпляр класса, и он автоматически передается в качестве первого аргумента. Однако наш `ValidatedFunction` не обрабатывает этот параметр `self` правильно, потому что он не знает, что его используют как метод.

**Понимание проблемы**

Когда вы определяете метод внутри класса и затем заменяете его на `ValidatedFunction`, вы, по сути, оборачиваете исходный метод. Проблема в том, что обернутый метод не автоматически обрабатывает параметр `self` правильно. Он ожидает аргументы таким образом, что не учитывает передачу экземпляра в качестве первого аргумента.

**Решение проблемы**

Чтобы решить эту проблему, нам нужно изменить способ обработки методов. Мы создадим новый класс с именем `ValidatedMethod`, который может правильно обрабатывать вызовы методов. Добавьте следующий код в конец файла `validate.py`:

```python
import inspect

class ValidatedMethod:
    def __init__(self, func):
        self.func = func
        self.signature = inspect.signature(func)

    def __get__(self, instance, owner):
        # This method is called when the attribute is accessed as a method
        if instance is None:
            return self

        # Return a callable that binds 'self' to the instance
        def method_wrapper(*args, **kwargs):
            return self(instance, *args, **kwargs)

        return method_wrapper

    def __call__(self, instance, *args, **kwargs):
        # Bind the arguments to the function parameters
        bound = self.signature.bind(instance, *args, **kwargs)

        # Validate each argument against its annotation
        for name, val in bound.arguments.items():
            if name in self.func.__annotations__:
                # Get the validator class from the annotation
                validator = self.func.__annotations__[name]
                # Apply the validation
                validator.check(val)

        # Call the function with the validated arguments
        return self.func(instance, *args, **kwargs)
```

Теперь нам нужно изменить класс `Stock`, чтобы использовать `ValidatedMethod` вместо `ValidatedFunction`. Откройте файл `stock.py` снова:

```bash
code /home/labex/project/stock.py
```

Обновите класс `Stock` следующим образом:

```python
from validate import ValidatedMethod, Integer

class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @property
    def cost(self):
        return self.shares * self.price

    @ValidatedMethod
    def sell(self, nshares: Integer):
        self.shares -= nshares
```

Класс `ValidatedMethod` является дескриптором, который представляет собой особый тип объекта в Python, который может изменить способ доступа к атрибутам. Метод `__get__` вызывается, когда атрибут доступен как метод. Он возвращает вызываемый объект, который правильно передает экземпляр в качестве первого аргумента.

Запустите тестовый файл снова с помощью следующей команды:

```bash
python3 /home/labex/project/test_stock.py
```

Теперь вы должны увидеть вывод, похожий на следующий:

```
Initial shares: 100
Initial cost: $49010.0
After selling, shares: 90
After selling, cost: $44109.0
```

Эта задача показала вам важный аспект вызываемых объектов. При использовании их в качестве методов в классе они требуют особой обработки. Реализуя протокол дескриптора с методом `__get__`, мы можем создать вызываемые объекты, которые работают правильно как в качестве самостоятельных функций, так и в качестве методов.
