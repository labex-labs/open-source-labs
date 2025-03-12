# Понимание протокола дескрипторов

На этом этапе мы узнаем, как работают дескрипторы в Python, создав простой класс `Stock`. Дескрипторы в Python - это мощная возможность, которая позволяет настроить, как осуществляется доступ к атрибутам, как они устанавливаются и удаляются. Протокол дескрипторов состоит из трех специальных методов: `__get__()`, `__set__()` и `__delete__()`. Эти методы определяют, как дескриптор ведет себя при доступе к атрибуту, при присвоении ему значения или при удалении, соответственно.

Сначала нам нужно создать новый файл с именем `stock.py` в директории проекта. Этот файл будет содержать наш класс `Stock`. Вот код, который вы должны поместить в файл `stock.py`:

```python
# stock.py

class Stock:
    __slots__ = ['_name', '_shares', '_price']

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._name = value

    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, value):
        if not isinstance(value, int):
            raise TypeError('Expected an integer')
        if value < 0:
            raise ValueError('Expected a positive value')
        self._shares = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError('Expected a number')
        if value < 0:
            raise ValueError('Expected a positive value')
        self._price = value

    def cost(self):
        return self.shares * self.price

    def sell(self, amount):
        self.shares -= amount

    def __repr__(self):
        return f'Stock({self.name!r}, {self.shares!r}, {self.price!r})'
```

В этом классе `Stock` мы используем декоратор `property` для определения методов-геттеров и сеттеров для атрибутов `name`, `shares` и `price`. Эти методы-геттеры и сеттеры действуют как дескрипторы, что означает, что они контролируют, как к этим атрибутам осуществляется доступ и как они устанавливаются. Например, методы-сеттеры валидируют входные значения, чтобы убедиться, что они имеют правильный тип и находятся в приемлемом диапазоне.

Теперь, когда наш файл `stock.py` готов, откроем оболочку Python, чтобы поэкспериментировать с классом `Stock` и увидеть, как работают дескрипторы на практике. Для этого откройте терминал и выполните следующие команды:

```bash
cd ~/project
python3 -i stock.py
```

Опция `-i` в команде `python3` сообщает Python запустить интерактивную оболочку после выполнения файла `stock.py`. Таким образом, мы можем напрямую взаимодействовать с классом `Stock`, который мы только что определили.

В оболочке Python создадим объект акции и попробуем получить доступ к его атрибутам. Вот как это можно сделать:

```python
s = Stock('GOOG', 100, 490.10)
s.name      # Should return 'GOOG'
s.shares    # Should return 100
```

Когда вы получаете доступ к атрибутам `name` и `shares` объекта `s`, Python на самом деле использует метод `__get__` дескриптора в фоновом режиме. Декораторы `property` в нашем классе реализованы с использованием дескрипторов, что означает, что они контролируют доступ к атрибутам и их присваивание.

Давайте взглянем более детально на словарь класса, чтобы увидеть объекты дескрипторов. Словарь класса содержит все атрибуты и методы, определенные в классе. Вы можете просмотреть ключи словаря класса с помощью следующего кода:

```python
Stock.__dict__.keys()
```

Вы должны увидеть вывод, похожий на следующий:

```
dict_keys(['__module__', '__slots__', '__init__', 'name', '_name', 'shares', '_shares', 'price', '_price', 'cost', 'sell', '__repr__', '__doc__'])
```

Ключи `name`, `shares` и `price` представляют объекты дескрипторов, созданные декораторами `property`.

Теперь давайте рассмотрим, как работают дескрипторы, вызвав их методы вручную. В качестве примера мы будем использовать дескриптор `shares`. Вот как это можно сделать:

```python
# Get the descriptor object for 'shares'
q = Stock.__dict__['shares']

# Use the __get__ method to retrieve the value
q.__get__(s, Stock)  # Should return 100

# Use the __set__ method to set a new value
q.__set__(s, 75)
s.shares  # Should now be 75

# Try to set an invalid value
try:
    q.__set__(s, '75')  # Should raise TypeError
except TypeError as e:
    print(f"Error: {e}")
```

Когда вы получаете доступ к атрибуту, такому как `s.shares`, Python вызывает метод `__get__` дескриптора, чтобы получить значение. Когда вы присваиваете значение, как в `s.shares = 75`, Python вызывает метод `__set__` дескриптора. Затем дескриптор может проверить данные и вызвать ошибки, если входное значение не является допустимым.

После того, как вы закончите экспериментировать с классом `Stock` и дескрипторами, вы можете выйти из оболочки Python, выполнив следующую команду:

```python
exit()
```
