# Importar as bibliotecas necessárias e carregar os dados

Primeiramente, precisamos importar as bibliotecas Python necessárias e carregar os dados de qualidade do ar. Os dados serão lidos em um DataFrame do pandas, que é uma estrutura de dados rotulada bidimensional.

```python
# import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# load the air quality data
air_quality = pd.read_csv("data/air_quality_no2_long.csv")

# rename the "date.utc" column to "datetime"
air_quality = air_quality.rename(columns={"date.utc": "datetime"})
```
