# Создаем примерные данные

Далее мы создадим примерные данные для использования на графике. В этом примере мы будем использовать функцию `numpy.arange()` для создания массива значений от 0,1 до 4 с шагом 0,5. Затем мы используем функцию `numpy.exp()` для вычисления экспоненты каждого значения в массиве.

```python
# example data
x = np.arange(0.1, 4, 0.5)
y = np.exp(-x)
```
