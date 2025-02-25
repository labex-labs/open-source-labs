# Генерировать случайные данные

Мы сгенерируем некоторые случайные данные, которые будут использоваться для точечного графика и гистограмм.

```python
# Fixing random state for reproducibility
np.random.seed(19680801)

# Generate random data
x = np.random.randn(1000)
y = np.random.randn(1000)
```
