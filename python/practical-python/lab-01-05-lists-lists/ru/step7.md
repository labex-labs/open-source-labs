# Упражнение 1.19: Извлечение и перезапись элементов списка

Попробуйте несколько обращений по индексу:

```python
>>> symlist[0]
'HPQ'
>>> symlist[1]
'AAPL'
>>> symlist[-1]
'GOOG'
>>> symlist[-2]
'DOA'
>>>
```

Попробуйте перезаписать одно значение:

```python
>>> symlist[2] = 'AIG'
>>> symlist
['HPQ', 'AAPL', 'AIG', 'MSFT', 'YHOO', 'DOA', 'GOOG']
>>>
```

Возьмите несколько срезов:

```python
>>> symlist[0:3]
['HPQ', 'AAPL', 'AIG']
>>> symlist[-2:]
['DOA', 'GOOG']
>>>
```

Создайте пустой список и добавьте в него элемент.

```python
>>> mysyms = []
>>> mysyms.append('GOOG')
>>> mysyms
['GOOG']
```

Вы можете перезаписать часть списка другим списком. Например:

```python
>>> symlist[-2:] = mysyms
>>> symlist
['HPQ', 'AAPL', 'AIG', 'MSFT', 'YHOO', 'GOOG']
>>>
```

Когда вы это делаете, список слева (`symlist`) будет изменен размером в соответствии с тем, чтобы вместить список справа (`mysyms`). Например, в вышеприведенном примере последние два элемента `symlist` были заменены одним элементом списка `mysyms`.
