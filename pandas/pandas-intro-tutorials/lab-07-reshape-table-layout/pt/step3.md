# Converter Formato de Tabela Longo para Largo

Agora, converteremos os dados em formato longo de qualidade do ar para formato largo usando a função `pivot`.

```python
# Filtrar apenas dados no2
no2 = air_quality[air_quality["parameter"] == "no2"]

# Usar 2 medições (head) para cada localização (groupby)
no2_subset = no2.sort_index().groupby(["location"]).head(2)

# Pivotar os dados
no2_subset.pivot(columns="location", values="value")
```
