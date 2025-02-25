# Загружаем данные изображения

Мы будем использовать пример данных изображения под названием `bivariate_normal.npy` из `cbook`, чтобы продемонстрировать ImageGrid. Мы загружаем данные изображения с использованием функции `get_sample_data` из `cbook`.

```python
Z = cbook.get_sample_data("axes_grid/bivariate_normal.npy")
im1 = Z
im2 = Z[:, :10]
im3 = Z[:, 10:]
vmin, vmax = Z.min(), Z.max()
```
