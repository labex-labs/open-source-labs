# Construir el conjunto de datos

El primer paso es construir el conjunto de datos a partir de los datos de muestra de aire recolectados en el Observatorio de Mauna Loa. Estamos interesados en estimar la concentración de CO2 y extrapolarla para años futuros. Cargamos el conjunto de datos original disponible en OpenML y preprocesamos el conjunto de datos calculando la media mensual y eliminando los meses para los que no se recogieron mediciones.

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
