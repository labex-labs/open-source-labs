# Задайте случайный сид и интервалы

Установите случайный сид для воспроизводимости и задайте края интервалов.

```python
# Fixing random state for reproducibility
np.random.seed(19680801)

# Fixing bin edges
HIST_BINS = np.linspace(-4, 4, 100)
```
