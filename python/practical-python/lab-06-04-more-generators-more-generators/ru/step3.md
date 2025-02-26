# Модуль `itertools`

`itertools` - это библиотечный модуль с различными функциями, предназначенными для помощи в работе с итераторами/генераторами.

```python
itertools.chain(s1,s2)
itertools.count(n)
itertools.cycle(s)
itertools.dropwhile(predicate, s)
itertools.groupby(s)
itertools.ifilter(predicate, s)
itertools.imap(function, s1,... sN)
itertools.repeat(s, n)
itertools.tee(s, ncopies)
itertools.izip(s1,..., sN)
```

Все функции обрабатывают данные итеративно. Они реализуют различные виды итерационных паттернов.

Больше информации в руководстве [Generator Tricks for Systems Programmers](http://www.dabeaz.com/generators/) из PyCon '08.

В предыдущих упражнениях вы писали код, который следил за строками, записываемыми в файл журнала, и анализировал их в последовательность строк. В этом упражнении продолжаем развивать этот код. Убедитесь, что `stocksim.py` по-прежнему работает.
