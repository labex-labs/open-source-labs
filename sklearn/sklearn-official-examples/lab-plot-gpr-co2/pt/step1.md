# Criar o Conjunto de Dados

O primeiro passo é criar o conjunto de dados, derivando-o das amostras de ar coletadas no Observatório Mauna Loa. Estamos interessados em estimar a concentração de CO2 e extrapolá-la para anos futuros. Carregamos o conjunto de dados original disponível no OpenML e pré-processamos o conjunto de dados calculando a média mensal e removendo os meses sem medições.

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
