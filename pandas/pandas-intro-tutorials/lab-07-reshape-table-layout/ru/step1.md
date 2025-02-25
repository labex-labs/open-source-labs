# Импорт библиотек и загрузка данных

Сначала импортируем необходимые библиотеки и загрузим наборы данных.

```python
import pandas as pd

# Загрузка набора данных о титанике
titanic = pd.read_csv("data/titanic.csv")

# Загрузка набора данных о качестве воздуха
air_quality = pd.read_csv("data/air_quality_long.csv", index_col="date.utc", parse_dates=True)
```
