# Получить демо-изображение

В этом шаге мы определим функцию для получения демо-изображения и его области. Мы будем использовать функцию `get_sample_data()` из `cbook`, чтобы получить пример изображения.

```python
def get_demo_image():
    z = cbook.get_sample_data("axes_grid/bivariate_normal.npy")  # 15x15 array
    return z, (-3, 4, -4, 3)
```
