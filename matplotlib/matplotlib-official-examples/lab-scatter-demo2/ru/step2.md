# Загружаем данные

Мы загрузим numpy record array из данных csv yahoo с полями date, open, high, low, close, volume, adj_close из директории mpl-data/sample_data. В record array дата хранится в виде np.datetime64 с единицей измерения день ('D') в колонке date.

```python
import matplotlib.cbook as cbook

price_data = cbook.get_sample_data('goog.npz')['price_data'].view(np.recarray)
price_data = price_data[-250:]  # get the most recent 250 trading days
```
