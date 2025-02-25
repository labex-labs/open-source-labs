# Импортируем необходимые библиотеки и данные

Сначала нам нужно импортировать необходимые библиотеки, которые это `matplotlib`, `numpy` и `matplotlib.cbook`. Также нам нужно загрузить массив записей `numpy` из данных CSV Yahoo с полями `date`, `open`, `high`, `low`, `close`, `volume`, `adj_close` из директории `mpl-data/sample_data`. В массиве записей дата хранится в виде `np.datetime64` с единицей измерения день ('D') в столбце `date`. Мы будем использовать эти данные для построения финансового временного ряда.

```python
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cbook as cbook

# Загружаем данные из директории sample_data
r = cbook.get_sample_data('goog.npz')['price_data'].view(np.recarray)
r = r[:9]  # берём первые 9 дней
```
