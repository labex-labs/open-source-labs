# Criar uma Nova Coluna

Criaremos uma nova coluna, "london_mg_per_cubic", multiplicando a coluna "station_london" por um fator de conversão.

```python
# Criar nova coluna multiplicando "station_london" por fator de conversão
air_quality["london_mg_per_cubic"] = air_quality["station_london"] * 1.882
```
