# Cargar los datos

Para este tutorial, utilizaremos datos de calidad del aire. Los datos se cargarán desde un archivo CSV en un DataFrame de Pandas.

```python
# Cargando los datos
air_quality = pd.read_csv("data/air_quality_no2.csv", index_col=0, parse_dates=True)
air_quality.head()
```
