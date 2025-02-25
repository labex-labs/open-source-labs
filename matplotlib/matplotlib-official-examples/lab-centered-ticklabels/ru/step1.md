# Загрузка финансовых данных

Сначала нам нужно загрузить некоторые финансовые данные о цене акций Google с использованием функции `cbook.get_sample_data()` из Matplotlib. Мы будем использовать данные за последние 250 дней.

```python
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cbook as cbook

# Load some financial data; Google's stock price
r = cbook.get_sample_data('goog.npz')['price_data'].view(np.recarray)
r = r[-250:]  # get the last 250 days
```
