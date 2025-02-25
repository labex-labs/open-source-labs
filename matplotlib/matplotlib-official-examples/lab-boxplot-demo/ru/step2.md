# Генерируем данные

Далее мы сгенерируем некоторые образцовые данные, которые будем использовать в наших ящиках с усами. Для этого урока мы будем использовать следующие данные:

```python
spread = np.random.rand(50) * 100
center = np.ones(25) * 50
flier_high = np.random.rand(10) * 100 + 100
flier_low = np.random.rand(10) * -100
data = np.concatenate((spread, center, flier_high, flier_low))
```
