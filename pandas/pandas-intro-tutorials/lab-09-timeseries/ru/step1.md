# Импортируем необходимые библиотеки и загружаем данные

Сначала нам нужно импортировать необходимые библиотеки Python и загрузить данные о качестве воздуха. Данные будут прочитаны в DataFrame библиотеки pandas, который представляет собой двухмерную структуру данных с метками.

```python
# import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# load the air quality data
air_quality = pd.read_csv("data/air_quality_no2_long.csv")

# rename the "date.utc" column to "datetime"
air_quality = air_quality.rename(columns={"date.utc": "datetime"})
```
