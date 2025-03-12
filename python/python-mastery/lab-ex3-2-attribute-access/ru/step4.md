# Понимание связанных методов в Python

В Python методы представляют собой особый тип атрибутов, которые можно вызывать. Когда вы обращаетесь к методу через объект, вы получаете то, что называется "связанным методом". Связанный метод - это по сути метод, привязанный к определенному объекту. Это означает, что он имеет доступ к данным объекта и может выполнять операции над ними.

## Обращение к методам как к атрибутам

Начнем изучение связанных методов с использованием нашего класса `Stock`. Сначала посмотрим, как обратиться к методу как к атрибуту объекта.

```python
# Open a Python interactive shell
python3

# Import the Stock class and create a stock object
from stock import Stock
s = Stock('GOOG', 100, 490.10)

# Access the cost method without calling it
cost_method = s.cost
print(cost_method)  # Output: <bound method Stock.cost of <stock.Stock object at 0x...>>

# Call the method
result = cost_method()
print(result)  # Output: 49010.0

# You can also do this in one step
print(s.cost())  # Output: 49010.0
```

В приведенном выше коде мы сначала импортируем класс `Stock` и создаем его экземпляр. Затем мы обращаемся к методу `cost` объекта `s`, не вызывая его. Это дает нам связанный метод. Когда мы вызываем этот связанный метод, он вычисляет стоимость на основе данных объекта. Вы также можете напрямую вызвать метод у объекта за один шаг.

## Использование `getattr()` с методами

Другой способ обращения к методам - использование функции `getattr()`. Эта функция позволяет получить атрибут объекта по его имени.

```python
# Get the cost method using getattr
cost_method = getattr(s, 'cost')
print(cost_method)  # Output: <bound method Stock.cost of <stock.Stock object at 0x...>>

# Call the method
result = cost_method()
print(result)  # Output: 49010.0

# Get and call in one step
result = getattr(s, 'cost')()
print(result)  # Output: 49010.0
```

Здесь мы используем `getattr()` для получения метода `cost` из объекта `s`. Как и раньше, мы можем вызвать связанный метод, чтобы получить результат. И вы даже можете получить и вызвать метод в одной строке.

## Связанный метод и его объект

Связанный метод всегда хранит ссылку на объект, из которого он был получен. Это означает, что даже если вы сохраняете метод в переменной, он все еще знает, к какому объекту он принадлежит, и может получить доступ к данным этого объекта.

```python
# Store the cost method in a variable
c = s.cost

# Call the method
print(c())  # Output: 49010.0

# Change the object's state
s.shares = 75

# Call the method again - it sees the updated state
print(c())  # Output: 36757.5
```

В этом примере мы сохраняем метод `cost` в переменной `c`. Когда мы вызываем `c()`, он вычисляет стоимость на основе текущих данных объекта. Затем мы изменяем атрибут `shares` объекта `s`. Когда мы вызываем `c()` снова, он использует обновленные данные для вычисления новой стоимости.

## Исследование внутреннего устройства связанного метода

Связанный метод имеет два важных атрибута, которые дают нам больше информации о нем.

- `__self__`: Этот атрибут ссылается на объект, к которому метод привязан.
- `__func__`: Этот атрибут представляет собой фактический объект функции, которая представляет метод.

```python
# Get the cost method
c = s.cost

# Examine the bound method attributes
print(c.__self__)  # Output: <stock.Stock object at 0x...>
print(c.__func__)  # Output: <function Stock.cost at 0x...>

# You can manually call the function with the object
print(c.__func__(c.__self__))  # Output: 36757.5 (same as c())
```

Здесь мы обращаемся к атрибутам `__self__` и `__func__` связанного метода `c`. Мы видим, что `__self__` - это объект `s`, а `__func__` - это функция `cost`. Мы даже можем вручную вызвать функцию, передав объект в качестве аргумента, и получим тот же результат, что и при вызове связанного метода напрямую.

## Пример с методом, принимающим аргументы

Посмотрим, как связанные методы работают с методом, принимающим аргументы, например, методом `sell()`.

```python
# Get the sell method
sell_method = s.sell

# Examine the method
print(sell_method)  # Output: <bound method Stock.sell of <stock.Stock object at 0x...>>

# Call the method with an argument
sell_method(25)
print(s.shares)  # Output: 50

# Call the method manually using __func__ and __self__
sell_method.__func__(sell_method.__self__, 10)
print(s.shares)  # Output: 40
```

В этом примере мы получаем метод `sell` как связанный метод. Когда мы вызываем его с аргументом, он обновляет атрибут `shares` объекта `s`. Мы также можем вручную вызвать метод, используя атрибуты `__func__` и `__self__`, передав также аргумент.

Понимание связанных методов помогает понять, как работает объектная система Python "под капотом", что может быть полезно для отладки, метапрограммирования и создания сложных программистских шаблонов.
