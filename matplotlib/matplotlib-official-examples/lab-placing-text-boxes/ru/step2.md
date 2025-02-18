# Создание данных

В этом примере мы создадим случайный набор данных с использованием `numpy.random.randn()`.

```python
np.random.seed(19680801)
x = 30*np.random.randn(10000)
mu = x.mean()
median = np.median(x)
sigma = x.std()
```
