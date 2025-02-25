# Importieren der erforderlichen Bibliotheken und Laden der Daten

Zunächst müssen wir die erforderlichen Python-Bibliotheken importieren und die Luftqualitätsdaten laden. Die Daten werden in einen pandas-DataFrame eingelesen, der eine zweidimensionale gelabelte Datenstruktur ist.

```python
# import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# load the air quality data
air_quality = pd.read_csv("data/air_quality_no2_long.csv")

# rename the "date.utc" column to "datetime"
air_quality = air_quality.rename(columns={"date.utc": "datetime"})
```
