# Создать искусственные данные

Нам нужно создать некоторые искусственные данные для построения графика. В этом практическом занятии мы построим логарифм частоты (в герцах) по отношению к логарифму мощности (в ваттах). Мы будем использовать библиотеку `numpy` для генерации данных.

```python
# Fixing random state for reproducibility
prng = np.random.RandomState(19680801)

# Create artificial data to plot.
# The x data span over several decades to demonstrate several SI prefixes.
xs = np.logspace(1, 9, 100)
ys = (0.8 + 0.4 * prng.uniform(size=100)) * np.log10(xs)**2
```
