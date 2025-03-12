# Улучшение реализации дескрипторов

На этом этапе мы усовершенствуем нашу реализацию дескрипторов. Возможно, вы заметили, что в некоторых случаях мы избыточно указываем имена. Это может сделать наш код немного запутанным и трудным для поддержки. Чтобы решить эту проблему, мы воспользуемся методом `__set_name__`, полезной функцией, введенной в Python 3.6.

Метод `__set_name__` вызывается автоматически при определении класса. Его основная задача - установить имя дескриптора за нас, так что нам не нужно делать это вручную каждый раз. Это сделает наш код чище и более эффективным.

Теперь обновим файл `validate.py`, чтобы он включал метод `__set_name__`. Вот как будет выглядеть обновленный код:

```python
# validate.py

class Validator:
    def __init__(self, name=None):
        self.name = name

    def __set_name__(self, cls, name):
        # This gets called when the class is defined
        # It automatically sets the name of the descriptor
        if self.name is None:
            self.name = name

    @classmethod
    def check(cls, value):
        return value

    def __set__(self, instance, value):
        instance.__dict__[self.name] = self.check(value)


class String(Validator):
    expected_type = str

    @classmethod
    def check(cls, value):
        if not isinstance(value, cls.expected_type):
            raise TypeError(f'Expected {cls.expected_type}')
        return value


class PositiveInteger(Validator):
    expected_type = int

    @classmethod
    def check(cls, value):
        if not isinstance(value, cls.expected_type):
            raise TypeError(f'Expected {cls.expected_type}')
        if value < 0:
            raise ValueError('Expected a positive value')
        return value


class PositiveFloat(Validator):
    expected_type = float

    @classmethod
    def check(cls, value):
        if not isinstance(value, (int, float)):
            raise TypeError('Expected a number')
        if value < 0:
            raise ValueError('Expected a positive value')
        return float(value)
```

В приведенном выше коде метод `__set_name__` в классе `Validator` проверяет, является ли атрибут `name` равным `None`. Если это так, он устанавливает `name` равным фактическому имени атрибута, используемому в определении класса. Таким образом, нам не нужно явно указывать имя при создании экземпляров классов дескрипторов.

Теперь, когда мы обновили файл `validate.py`, мы можем создать улучшенную версию нашего класса `Stock`. В этой новой версии нам не нужно будет избыточно указывать имена. Вот код улучшенного класса `Stock`:

```python
# improved_stock.py

from validate import String, PositiveInteger, PositiveFloat

class Stock:
    name = String()  # No need to specify 'name' anymore
    shares = PositiveInteger()
    price = PositiveFloat()

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price

    def sell(self, amount):
        self.shares -= amount

    def __repr__(self):
        return f'Stock({self.name!r}, {self.shares!r}, {self.price!r})'
```

В этом классе `Stock` мы просто создаем экземпляры классов дескрипторов `String`, `PositiveInteger` и `PositiveFloat` без указания имен. Метод `__set_name__` в классе `Validator` автоматически позаботится о установке имен.

Давайте протестируем наш улучшенный класс `Stock`. Сначала откройте терминал и перейдите в директорию проекта. Затем запустите файл `improved_stock.py` в интерактивном режиме. Вот команды для этого:

```bash
cd ~/project
python3 -i improved_stock.py
```

Как только вы войдете в интерактивную сессию Python, вы можете попробовать следующие команды, чтобы протестировать функциональность класса `Stock`:

```python
s = Stock('GOOG', 100, 490.10)
print(s.name)    # Should return 'GOOG'
print(s.shares)  # Should return 100
print(s.price)   # Should return 490.1

# Try changing values
s.shares = 75
print(s.shares)  # Should return 75

# Try invalid values
try:
    s.shares = '75'  # Should raise TypeError
except TypeError as e:
    print(f"Error: {e}")

try:
    s.price = -10.5  # Should raise ValueError
except ValueError as e:
    print(f"Error: {e}")

exit()
```

Эти команды создают экземпляр класса `Stock`, выводят его атрибуты, изменяют значение атрибута, а затем пытаются установить недопустимые значения, чтобы проверить, вызываются ли соответствующие ошибки.

Метод `__set_name__` автоматически устанавливает имя дескриптора при определении класса. Это делает ваш код чище и менее избыточным, так как вам больше не нужно указывать имя атрибута дважды.

Это улучшение демонстрирует, как протокол дескрипторов Python продолжает развиваться, делая проще написание чистого и поддерживаемого кода.
