# Создание датасета

Первым шагом является создание датасета путём извлечения данных с обсерватории Мауна-Лоа, где собирались пробы воздуха. Нас интересует оценка концентрации CO2 и её экстраполяция на будущие годы. Мы загружаем исходный датасет, доступный в OpenML, и предобрабатываем датасет, вычисляя месячные средние значения и удаляя месяцы, для которых не были произведены измерения.

```python
from sklearn.datasets import fetch_openml
import pandas as pd

co2 = fetch_openml(data_id=41187, as_frame=True, parser="pandas")
co2_data = co2.frame
co2_data["date"] = pd.to_datetime(co2_data[["year", "month", "day"]])
co2_data = co2_data[["date", "co2"]].set_index("date")
co2_data = co2_data.resample("M").mean().dropna(axis="index", how="any")

X = (co2_data.index.year + co2_data.index.month / 12).to_numpy().reshape(-1, 1)
y = co2_data["co2"].to_numpy()
```
