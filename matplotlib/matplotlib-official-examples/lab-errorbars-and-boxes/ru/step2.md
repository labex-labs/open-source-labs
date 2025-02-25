# Подготовка данных

Затем мы подготовим данные для нашего ящика с усами. Мы создадим некоторые фиктивные данные для значений x и y, а также для значений ошибок.

```python
# Number of data points
n = 5

# Dummy data
np.random.seed(19680801)
x = np.arange(0, n, 1)
y = np.random.rand(n) * 5.

# Dummy errors (above and below)
xerr = np.random.rand(2, n) + 0.1
yerr = np.random.rand(2, n) + 0.2
```
