# Importar Pandas y cargar datos

Primero, importaremos la biblioteca de pandas y cargaremos los datos de calidad del aire desde un archivo CSV.

```python
# Importar la biblioteca de pandas
import pandas as pd

# Cargar los datos de calidad del aire
air_quality = pd.read_csv("data/air_quality_no2.csv", index_col=0, parse_dates=True)
```
