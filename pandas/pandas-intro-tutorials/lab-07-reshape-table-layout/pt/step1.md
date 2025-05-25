# Importar Bibliotecas e Carregar Dados

Primeiramente, vamos importar as bibliotecas necessárias e carregar os conjuntos de dados.

```python
import pandas as pd

# Carregar o conjunto de dados Titanic
titanic = pd.read_csv("data/titanic.csv")

# Carregar o conjunto de dados Qualidade do Ar
air_quality = pd.read_csv("data/air_quality_long.csv", index_col="date.utc", parse_dates=True)
```
