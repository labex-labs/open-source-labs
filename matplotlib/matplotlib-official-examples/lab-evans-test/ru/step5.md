# Создайте точки данных

В этом шаге мы создадим несколько точек данных с использованием класса пользовательских единиц - `Foo`.

```python
# create some Foos
x = [Foo(val, 1.0) for val in range(0, 50, 2)]
# and some arbitrary y data
y = [i for i in range(len(x))]
```
