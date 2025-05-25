# Mesclar Tabelas Usando um Identificador Comum

Em seguida, adicionaremos as coordenadas das estações à tabela de medições usando a função `merge`. Realizaremos um _left join_ na coluna `location`.

```python
# Load the stations coordinates data
stations_coord = pd.read_csv("data/air_quality_stations.csv")

# Merge the air_quality and stations_coord dataframes
air_quality = pd.merge(air_quality, stations_coord, how="left", on="location")
```
