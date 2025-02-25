# Создать данные

Далее мы создадим некоторые случайные данные для использования в нашей визуализации. В этом примере мы создадим два массива случайных данных с использованием numpy.

```python
# Fixing random state for reproducibility
np.random.seed(19680801)

x = np.random.rand(20)
y = 1e7 * np.random.rand(20)
```
