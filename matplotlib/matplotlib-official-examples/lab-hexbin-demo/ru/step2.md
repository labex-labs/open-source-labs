# Генерация данных

Мы сгенерируем 100 000 точек данных с использованием `numpy.random.standard_normal()` и `numpy.random.standard_normal()`. `standard_normal()` генерирует случайные числа из стандартного нормального распределения с математическим ожиданием 0 и стандартным отклонением 1.

```python
np.random.seed(19680801)

n = 100_000
x = np.random.standard_normal(n)
y = 2.0 + 3.0 * x + 4.0 * np.random.standard_normal(n)
xlim = x.min(), x.max()
ylim = y.min(), y.max()
```
