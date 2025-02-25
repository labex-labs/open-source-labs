# Importar las bibliotecas necesarias y cargar los datos

Primero, necesitamos importar las bibliotecas de Python requeridas y cargar los datos de calidad del aire. Los datos se leerán en un DataFrame de pandas, que es una estructura de datos etiquetada bidimensional.

```python
# import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# load the air quality data
air_quality = pd.read_csv("data/air_quality_no2_long.csv")

# rename the "date.utc" column to "datetime"
air_quality = air_quality.rename(columns={"date.utc": "datetime"})
```
