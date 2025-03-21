# Работа со словарями в Python

В Python словари являются фундаментальной структурой данных. Они представляют собой хранилища ключ - значение, то есть позволяют сопоставить одно значение (значение) с другим (ключом). Это чрезвычайно полезно при работе с данными, которые имеют естественные отношения типа ключ - значение. Например, вы можете сопоставить имя человека (ключ) с его возрастом (значением), или, как мы увидим в этом разделе, сопоставить тикеры акций (ключи) с их ценами (значениями).

## Создание и доступ к словарям

Начнем с открытия новой интерактивной сессии Python. Это похоже на вход в специальную среду, где вы можете писать и запускать код Python построчно. Чтобы начать эту сессию, откройте терминал и введите следующую команду:

```bash
python3
```

После того, как вы находитесь в интерактивной сессии Python, вы можете создать словарь. В нашем случае мы создадим словарь, который сопоставляет тикеры акций с их ценами. Вот как это делается:

```python
>>> prices = {'IBM': 91.1, 'GOOG': 490.1, 'AAPL': 312.23}
>>> prices
{'IBM': 91.1, 'GOOG': 490.1, 'AAPL': 312.23}
```

В первой строке мы создаем словарь с именем `prices` и присваиваем ему несколько пар ключ - значение. Ключами являются тикеры акций (`IBM`, `GOOG`, `AAPL`), а значениями - соответствующие цены. Вторая строка просто показывает нам содержимое словаря `prices`.

Теперь давайте посмотрим, как получить доступ к значениям в словаре с помощью ключей и как их изменить.

```python
>>> prices['IBM']    # Получить значение для ключа 'IBM'
91.1

>>> prices['IBM'] = 123.45    # Обновить существующее значение
>>> prices
{'IBM': 123.45, 'GOOG': 490.1, 'AAPL': 312.23}

>>> prices['HPQ'] = 26.15    # Добавить новую пару ключ - значение
>>> prices
{'IBM': 123.45, 'GOOG': 490.1, 'AAPL': 312.23, 'HPQ': 26.15}
```

В первой строке мы получаем значение, связанное с ключом `IBM`. Во второй и третьей строках мы обновляем значение для ключа `IBM`, а затем добавляем новую пару ключ - значение (`HPQ` с ценой `26.15`).

## Получение ключей словаря

Иногда вам может понадобиться получить список всех ключей в словаре. Существует несколько способов сделать это.

```python
>>> list(prices)    # Преобразовать ключи словаря в список
['IBM', 'GOOG', 'AAPL', 'HPQ']
```

Здесь мы используем функцию `list()` для преобразования ключей словаря `prices` в список.

Вы также можете использовать метод `keys()`, который возвращает специальный объект, называемый `dict_keys`.

```python
>>> prices.keys()    # Возвращает объект dict_keys
dict_keys(['IBM', 'GOOG', 'AAPL', 'HPQ'])
```

## Получение значений словаря

Аналогично, вам может понадобиться получить все значения в словаре. Для этого вы можете использовать метод `values()`.

```python
>>> prices.values()    # Возвращает объект dict_values
dict_values([123.45, 490.1, 312.23, 26.15])
```

Этот метод возвращает объект `dict_values`, который содержит все значения в словаре `prices`.

## Удаление элементов

Если вы хотите удалить пару ключ - значение из словаря, вы можете использовать ключевое слово `del`.

```python
>>> del prices['AAPL']    # Удалить запись с ключом 'AAPL'
>>> prices
{'IBM': 123.45, 'GOOG': 490.1, 'HPQ': 26.15}
```

Здесь мы удаляем пару ключ - значение с ключом `AAPL` из словаря `prices`.

## Проверка наличия ключа

Для проверки наличия ключа в словаре вы можете использовать оператор `in`.

```python
>>> 'IBM' in prices
True
>>> 'AAPL' in prices
False
```

Оператор `in` возвращает `True`, если ключ существует в словаре, и `False` в противном случае.

## Методы словарей

Словари имеют несколько полезных методов. Рассмотрим несколько из них.

```python
>>> prices.get('MSFT', 0)    # Получить значение или значение по умолчанию, если ключа нет
0
>>> prices.get('IBM', 0)
123.45

>>> prices.update({'MSFT': 25.0, 'GOOG': 500.0})    # Обновить несколько значений
>>> prices
{'IBM': 123.45, 'GOOG': 500.0, 'HPQ': 26.15, 'MSFT': 25.0}
```

Метод `get()` пытается получить значение, связанное с ключом. Если ключа нет, он возвращает значение по умолчанию (в данном случае `0`). Метод `update()` используется для обновления нескольких пар ключ - значение в словаре сразу.

Когда вы закончите работу в интерактивной сессии Python, вы можете выйти из нее, введя:

```python
>>> exit()
```
