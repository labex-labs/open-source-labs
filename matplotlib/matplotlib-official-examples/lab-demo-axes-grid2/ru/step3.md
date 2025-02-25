# Подготовьте примерные данные

Мы будем использовать функцию `get_sample_data` из cbook для получения примерных данных. Затем мы подготовим изображения для отображения в сетке.

```python
Z = cbook.get_sample_data("axes_grid/bivariate_normal.npy")
extent = (-3, 4, -4, 3)
ZS = [Z[i::3, :] for i in range(3)]
extent = extent[0], extent[1]/3., extent[2], extent[3]
```
