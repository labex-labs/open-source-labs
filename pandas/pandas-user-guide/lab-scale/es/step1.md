# Generar Conjunto de Datos

El primer paso es generar un gran conjunto de datos para pruebas. Creamos un conjunto de datos con muchas columnas que se puede almacenar en un archivo parquet. Este paso requiere las bibliotecas pandas y numpy.

```python
import pandas as pd
import numpy as np

def make_timeseries(start="2000-01-01", end="2000-12-31", freq="1D", seed=None):
    # Función para generar datos de series temporales
    index = pd.date_range(start=start, end=end, freq=freq, name="timestamp")
    n = len(index)
    state = np.random.RandomState(seed)
    columns = {
        "name": state.choice(["Alice", "Bob", "Charlie"], size=n),
        "id": state.poisson(1000, size=n),
        "x": state.rand(n) * 2 - 1,
        "y": state.rand(n) * 2 - 1,
    }
    df = pd.DataFrame(columns, index=index, columns=sorted(columns))
    if df.index[-1] == end:
        df = df.iloc[:-1]
    return df

timeseries = [
    make_timeseries(freq="1T", seed=i).rename(columns=lambda x: f"{x}_{i}")
    for i in range(10)
]
ts_wide = pd.concat(timeseries, axis=1)
ts_wide.to_parquet("timeseries_wide.parquet")
```
