# Загружаем данные

Далее мы загружаем примерные данные о высоте с использованием функции `get_sample_data` из Matplotlib. Затем извлекаем данные о высоте и размер ячейки сетки.

```python
dem = get_sample_data('jacksboro_fault_dem.npz')
z = dem['elevation']
dx, dy = dem['dx'], dem['dy']
```
