# Загружаем данные

Далее мы загрузим данные, которые хотим отобразить. Мы будем использовать массив записей numpy из данных csv Yahoo с полями date, open, high, low, close, volume, adj_close из директории mpl-data/sample_data. В массиве записей дата хранится в виде np.datetime64 с единицей измерения день ('D') в столбце date.

```python
data = cbook.get_sample_data('goog.npz')['price_data']
```
