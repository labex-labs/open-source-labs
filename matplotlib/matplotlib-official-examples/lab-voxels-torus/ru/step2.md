# Определение функции для нахождения серединных точек

Далее мы определяем функцию `midpoints`, которая вычисляет серединные точки массива координат. Эта функция будет использоваться позже для вычисления серединных точек `r`, `theta` и `z`.

```python
def midpoints(x):
    sl = ()
    for i in range(x.ndim):
        x = (x[sl + np.index_exp[:-1]] + x[sl + np.index_exp[1:]]) / 2.0
        sl += np.index_exp[:]
    return x
```
