# Использование своего метакласса

Теперь мы создадим класс, который будет использовать наш метакласс через наследование. Это поможет нам понять, как вызывается метакласс при определении класса.

Метакласс в Python - это класс, который создает другие классы. Когда вы определяете класс, Python использует метакласс для построения объекта этого класса. С помощью наследования мы можем указать, какой метакласс должен использоваться классом.

1. Откройте файл `mymeta.py` и добавьте следующий код в конец файла:

```python
class Stock(myobject):
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares
```

Здесь мы определяем класс `Stock`, который наследуется от `myobject`. Метод `__init__` - это специальный метод в классах Python. Он вызывается при создании объекта класса и используется для инициализации атрибутов объекта. Метод `cost` вычисляет общую стоимость акций, а метод `sell` уменьшает количество акций.

2. Сохраните файл, нажав Ctrl+S. Сохранение файла гарантирует, что внесенные изменения будут сохранены и могут быть запущены позже.

3. Теперь давайте запустим файл, чтобы посмотреть, что произойдет. Откройте терминал в WebIDE и выполните следующие команды:

```bash
cd /home/labex/project
python3 mymeta.py
```

Команда `cd` изменяет текущую рабочую директорию на `/home/labex/project`, а `python3 mymeta.py` запускает Python - скрипт `mymeta.py`.

Вы должны увидеть вывод, похожий на следующий:

```
Creating class : myobject
Base classes   : ()
Attributes     : ['__module__', '__qualname__', '__doc__']
Creating class : Stock
Base classes   : (<class '__main__.myobject'>,)
Attributes     : ['__module__', '__qualname__', '__init__', 'cost', 'sell', '__doc__']
```

Этот вывод показывает, что наш метакласс вызывается при создании как класса `myobject`, так и класса `Stock`. Обратите внимание, что:

- Для класса `Stock` базовыми классами является `myobject`, так как `Stock` наследуется от `myobject`.
- Список атрибутов включает все определенные нами методы (`__init__`, `cost`, `sell`), а также некоторые атрибуты по умолчанию.

4. Давайте взаимодействуем с нашим классом `Stock`. Создайте новый файл с именем `test_stock.py` со следующим содержимым:

```python
# test_stock.py
from mymeta import Stock

# Create a new Stock instance
apple = Stock("AAPL", 100, 154.50)

# Use the methods
print(f"Stock: {apple.name}, Shares: {apple.shares}, Price: ${apple.price}")
print(f"Total cost: ${apple.cost()}")

# Sell some shares
apple.sell(10)
print(f"After selling 10 shares: {apple.shares} shares remaining")
print(f"Updated cost: ${apple.cost()}")
```

В этом коде мы импортируем класс `Stock` из модуля `mymeta`. Затем мы создаем экземпляр класса `Stock` с именем `apple`. Мы используем методы класса `Stock` для вывода информации о акциях, вычисления общей стоимости, продажи некоторых акций и вывода обновленной информации.

5. Запустите этот файл, чтобы протестировать наш класс `Stock`:

```bash
python3 test_stock.py
```

Вы должны увидеть вывод, похожий на следующий:

```
Creating class : myobject
Base classes   : ()
Attributes     : ['__module__', '__qualname__', '__doc__']
Creating class : Stock
Base classes   : (<class 'mymeta.myobject'>,)
Attributes     : ['__module__', '__qualname__', '__init__', 'cost', 'sell', '__doc__']
Stock: AAPL, Shares: 100, Price: $154.5
Total cost: $15450.0
After selling 10 shares: 90 shares remaining
Updated cost: $13905.0
```

Обратите внимание, что информация о нашем метаклассе выводится первой, за которой следует вывод из нашего тестового скрипта. Это происходит потому, что метакласс вызывается при определении класса, что происходит до выполнения кода в тестовом скрипте.
