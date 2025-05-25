# Adicionar a Descrição Completa e o Nome dos Parâmetros

Finalmente, adicionaremos a descrição completa e o nome dos parâmetros à tabela de medições. Realizamos um _left join_ nas colunas `parameter` e `id`.

```python
# Load the air quality parameters data
air_quality_parameters = pd.read_csv("data/air_quality_parameters.csv")

# Merge the air_quality and air_quality_parameters dataframes
air_quality = pd.merge(air_quality, air_quality_parameters, how='left', left_on='parameter', right_on='id')
```
