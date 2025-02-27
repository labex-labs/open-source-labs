# Das Dataset erstellen

Der erste Schritt besteht darin, das Dataset zu erstellen, indem es aus dem Mauna Loa Observatorium abgeleitet wird, das Luftproben gesammelt hat. Wir interessieren uns für die Schätzung der CO2-Konzentration und deren Extrapolation für weitere Jahre. Wir laden das ursprüngliche Dataset aus OpenML und verarbeiten das Dataset, indem wir einen monatlichen Mittelwert berechnen und Monate, für die keine Messungen durchgeführt wurden, ausschließen.

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
