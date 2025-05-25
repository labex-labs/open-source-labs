# Concatenando os Conjuntos de Dados

Em seguida, combinaremos as medições de Nitrato e Material Particulado em uma única tabela usando a função `concat`.

```python
# Concatenate the two dataframes
air_quality = pd.concat([air_quality_pm25, air_quality_no2], axis=0)
```
