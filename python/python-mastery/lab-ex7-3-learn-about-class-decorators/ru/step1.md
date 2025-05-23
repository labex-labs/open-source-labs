# Реализация проверки типов с использованием дескрипторов

На этом этапе мы создадим класс `Stock`, который будет использовать дескрипторы для проверки типов. Но сначала разберемся, что такое дескрипторы. Дескрипторы - это очень мощная возможность в Python. Они позволяют вам контролировать, как доступ к атрибутам классов осуществляется.

Дескрипторы - это объекты, которые определяют, как происходит доступ к атрибутам других объектов. Они делают это, реализуя специальные методы, такие как `__get__`, `__set__` и `__delete__`. Эти методы позволяют дескрипторам управлять тем, как атрибуты извлекаются, устанавливаются и удаляются. Дескрипторы очень полезны для реализации валидации, проверки типов и вычисляемых свойств. Например, вы можете использовать дескриптор, чтобы убедиться, что атрибут всегда является положительным числом или строкой определенного формата.

В файле `validate.py` уже есть классы валидаторов (`String`, `PositiveInteger`, `PositiveFloat`). Мы можем использовать эти классы для валидации атрибутов нашего класса `Stock`.

Теперь давайте создадим наш класс `Stock` с использованием дескрипторов.

1. Сначала откройте файл `stock.py` в редакторе. Вы можете сделать это, запустив следующую команду в терминале:

```bash
code ~/project/stock.py
```

Эта команда использует редактор `code` для открытия файла `stock.py`, расположенного в директории `~/project`.

2. После открытия файла замените заполнитель следующим кодом:

```python
# stock.py

from structure import Structure
from validate import String, PositiveInteger, PositiveFloat

class Stock(Structure):
    _fields = ('name', 'shares', 'price')
    name = String()
    shares = PositiveInteger()
    price = PositiveFloat()

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares

# Create an __init__ method based on _fields
Stock.create_init()
```

Разберем, что делает этот код. Кортеж `_fields` определяет атрибуты класса `Stock`. Это имена атрибутов, которые будут у объектов нашего класса `Stock`.

Атрибуты `name`, `shares` и `price` определены как объекты дескрипторов. Дескриптор `String()` гарантирует, что атрибут `name` является строкой. Дескриптор `PositiveInteger()` обеспечивает, чтобы атрибут `shares` был положительным целым числом. А дескриптор `PositiveFloat()` гарантирует, что атрибут `price` является положительным числом с плавающей точкой.

Свойство `cost` - это вычисляемое свойство. Оно вычисляет общую стоимость акций на основе количества акций и цены за одну акцию.

Метод `sell` используется для уменьшения количества акций. Когда вы вызываете этот метод с количеством акций для продажи, он вычитает это количество из атрибута `shares`.

Строка `Stock.create_init()` динамически создает метод `__init__` для нашего класса. Этот метод позволяет нам создавать объекты класса `Stock`, передав значения для атрибутов `name`, `shares` и `price`.

3. После добавления кода сохраните файл. Это обеспечит сохранение ваших изменений и их использование при запуске тестов.

4. Теперь давайте запустим тесты, чтобы проверить вашу реализацию. Сначала измените текущую директорию на `~/project`, запустив следующую команду:

```bash
cd ~/project
```

Затем запустите тесты с помощью следующей команды:

```bash
python3 teststock.py
```

Если ваша реализация правильная, вы должны увидеть вывод, похожий на следующий:

```
.........
----------------------------------------------------------------------
Ran 9 tests in 0.001s

OK
```

Этот вывод означает, что все тесты пройдены. Дескрипторы успешно валидируют типы каждого атрибута!

Давайте попробуем создать объект класса `Stock` в интерпретаторе Python. Сначала убедитесь, что вы находитесь в директории `~/project`. Затем запустите следующую команду:

```bash
cd ~/project
python3 -c "from stock import Stock; s = Stock('GOOG', 100, 490.1); print(s); print(f'Cost: {s.cost}')"
```

Вы должны увидеть следующий вывод:

```
Stock('GOOG', 100, 490.1)
Cost: 49010.0
```

Вы успешно реализовали дескрипторы для проверки типов! Теперь давайте усовершенствуем этот код еще больше.
