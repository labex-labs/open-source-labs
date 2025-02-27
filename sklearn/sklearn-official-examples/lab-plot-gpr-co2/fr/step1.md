# Construire l'ensemble de données

La première étape consiste à construire l'ensemble de données en le dérivant de l'Observatoire de Mauna Loa qui a collecté des échantillons d'air. Nous sommes intéressés à estimer la concentration de CO2 et à l'extrapoler pour les années suivantes. Nous chargeons l'ensemble de données original disponible sur OpenML et prétraitons l'ensemble de données en prenant la moyenne mensuelle et en éliminant les mois pour lesquels aucune mesure n'a été collectée.

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
