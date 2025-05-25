# Verificar a Razão dos Valores em Duas Colunas

Em seguida, verificaremos a razão dos valores nas colunas "station_paris" e "station_antwerp" e salvaremos o resultado em uma nova coluna.

```python
# Criar nova coluna dividindo "station_paris" por "station_antwerp"
air_quality["ratio_paris_antwerp"] = air_quality["station_paris"] / air_quality["station_antwerp"]
```
