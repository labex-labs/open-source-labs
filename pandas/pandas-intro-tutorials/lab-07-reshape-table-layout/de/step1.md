# Bibliotheken importieren und Daten laden

Zunächst importieren wir die erforderlichen Bibliotheken und laden die Datensätze.

```python
import pandas as pd

# Titanic-Datensatz laden
titanic = pd.read_csv("data/titanic.csv")

# Luftqualitäts-Datensatz laden
air_quality = pd.read_csv("data/air_quality_long.csv", index_col="date.utc", parse_dates=True)
```
