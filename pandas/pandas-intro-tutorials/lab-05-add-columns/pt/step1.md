# Importar Pandas e Carregar Dados

Primeiramente, importaremos a biblioteca pandas e carregaremos os dados de qualidade do ar de um arquivo CSV.

```python
# Importar a biblioteca pandas
import pandas as pd

# Carregar dados de qualidade do ar
air_quality = pd.read_csv("data/air_quality_no2.csv", index_col=0, parse_dates=True)
```
