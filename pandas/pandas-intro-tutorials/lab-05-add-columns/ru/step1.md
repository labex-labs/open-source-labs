# Импорт Pandas и загрузка данных

Сначала мы импортируем библиотеку pandas и загружаем данные о качестве воздуха из CSV-файла.

```python
# Import pandas library
import pandas as pd

# Load air quality data
air_quality = pd.read_csv("data/air_quality_no2.csv", index_col=0, parse_dates=True)
```
