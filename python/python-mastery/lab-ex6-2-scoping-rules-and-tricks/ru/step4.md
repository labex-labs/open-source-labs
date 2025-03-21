# Реализация продвинутой инициализации в структуре

Мы только что узнали две мощные техники для доступа к аргументам функции. Теперь мы используем эти техники для обновления нашего класса `Structure`. Сначала разберемся, почему мы это делаем. Эти техники сделают наш класс более гибким и легким в использовании, особенно при работе с разными типами аргументов.

Откройте файл `structure.py` в редакторе кода. Вы можете сделать это, запустив следующие команды в терминале. Команда `cd` изменяет текущую директорию на папку проекта, а команда `code` открывает файл `structure.py` в редакторе кода.

```bash
cd ~/project
code structure.py
```

Замените содержимое файла следующим кодом. Этот код определяет класс `Structure` с несколькими методами. Давайте разберем каждую часть, чтобы понять, что она делает.

```python
import sys

class Structure:
    _fields = ()

    @staticmethod
    def _init():
        # Get the caller's frame (the __init__ method that called this)
        frame = sys._getframe(1)

        # Get the local variables from that frame
        locs = frame.f_locals

        # Extract self and set other variables as attributes
        self = locs.pop('self')
        for name, val in locs.items():
            setattr(self, name, val)

    def __repr__(self):
        values = ', '.join(f'{name}={getattr(self, name)!r}' for name in self._fields)
        return f'{type(self).__name__}({values})'

    def __setattr__(self, name, value):
        if name.startswith('_') or name in self._fields:
            super().__setattr__(name, value)
        else:
            raise AttributeError(f'{type(self).__name__!r} has no attribute {name!r}')
```

Вот что мы сделали в коде:

1. Мы удалили старый метод `__init__()`. Поскольку подклассы будут определять свои собственные методы `__init__`, нам больше не нужен старый.
2. Мы добавили новый статический метод `_init()`. Этот метод использует инспекцию стека вызовов (frame inspection), чтобы автоматически захватить и установить все параметры в качестве атрибутов. Инспекция стека вызовов позволяет нам получить доступ к локальным переменным вызывающего метода.
3. Мы сохранили метод `__repr__()`. Этот метод предоставляет удобное строковое представление объекта, которое полезно для отладки и вывода.
4. Мы добавили метод `__setattr__()`. Этот метод обеспечивает валидацию атрибутов, гарантируя, что на объекте можно устанавливать только допустимые атрибуты.

Теперь обновим класс `Stock`. Откройте файл `stock.py` с помощью следующей команды:

```bash
code stock.py
```

Замените его содержимое следующим кодом:

```python
from structure import Structure

class Stock(Structure):
    _fields = ('name', 'shares', 'price')

    def __init__(self, name, shares, price):
        self._init()  # This magically captures and sets all parameters!

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares
```

Основное изменение здесь заключается в том, что наш метод `__init__` теперь вызывает `self._init()` вместо ручной установки каждого атрибута. Метод `_init()` использует инспекцию стека вызовов, чтобы автоматически захватить и установить все параметры в качестве атрибутов. Это делает код более компактным и легким в поддержке.

Протестируем нашу реализацию, запустив модульные тесты. Модульные тесты помогут нам убедиться, что наш код работает как ожидается. Запустите следующие команды в терминале:

```bash
cd ~/project
python3 teststock.py
```

Вы должны увидеть, что все тесты проходят, включая тест для именованных аргументов, который раньше не проходил. Это означает, что наша реализация работает правильно.

Также проверим справочную документацию для нашего класса `Stock`. Справочная документация предоставляет информацию о классе и его методах. Запустите следующую команду в терминале:

```bash
python3 -c "from stock import Stock; help(Stock)"
```

Теперь вы должны увидеть правильную сигнатуру для метода `__init__`, показывающую все имена параметров. Это делает проще для других разработчиков понять, как использовать класс.

Наконец, давайте интерактивно проверим, что именованные аргументы работают как ожидается. Запустите следующую команду в терминале:

```bash
python3 -c "from stock import Stock; s = Stock(name='GOOG', shares=100, price=490.1); print(s)"
```

Вы должны увидеть, что объект `Stock` корректно создан с указанными атрибутами. Это подтверждает, что наша система инициализации классов поддерживает именованные аргументы.

С этой реализацией мы создали гораздо более гибкую и удобную для пользователя систему инициализации классов, которая:

1. Сохраняет правильные сигнатуры функций в документации, что делает проще для разработчиков понять, как использовать класс.
2. Поддерживает как позиционные, так и именованные аргументы, обеспечивая больше гибкости при создании объектов.
3. Требует минимального количества шаблонного кода в подклассах, уменьшая количество кода, которое вам нужно написать.
