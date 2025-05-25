# Renomear os Rótulos das Colunas

Renomearemos os rótulos das colunas para corresponder aos identificadores das estações usados pelo OpenAQ.

```python
# Renomear os rótulos das colunas
air_quality_renamed = air_quality.rename(
    columns={
        "station_antwerp": "BETR801",
        "station_paris": "FR04014",
        "station_london": "London Westminster",
    }
)
```
