# Загрузка данных

Далее мы загрузим примерные данные, которые будем использовать в этом руководстве. Мы будем использовать файл `jacksboro_fault_dem.npz`, который содержит данные о высоте.

```python
dem = cbook.get_sample_data('jacksboro_fault_dem.npz')
elev = dem['elevation']
```
