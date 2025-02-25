# Importar bibliotecas y cargar datos

Primero, importemos las bibliotecas necesarias y carguemos los conjuntos de datos.

```python
import pandas as pd

# Cargar el conjunto de datos del Titanic
titanic = pd.read_csv("data/titanic.csv")

# Cargar el conjunto de datos de Calidad del Aire
air_quality = pd.read_csv("data/air_quality_long.csv", index_col="date.utc", parse_dates=True)
```
