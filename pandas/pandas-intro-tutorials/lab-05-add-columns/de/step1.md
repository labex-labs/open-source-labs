# Pandas importieren und Daten laden

Zunächst importieren wir die pandas-Bibliothek und laden die Luftqualitätsdaten aus einer CSV-Datei.

```python
# Import pandas library
import pandas as pd

# Load air quality data
air_quality = pd.read_csv("data/air_quality_no2.csv", index_col=0, parse_dates=True)
```
