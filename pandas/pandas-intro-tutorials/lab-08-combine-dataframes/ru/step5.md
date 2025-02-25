# Добавляем полное описание и имя параметров

Наконец, мы добавим полное описание и имя параметров в таблицу измерений. Мы выполняем левый внешний join по столбцам `parameter` и `id`.

```python
# Load the air quality parameters data
air_quality_parameters = pd.read_csv("data/air_quality_parameters.csv")

# Merge the air_quality and air_quality_parameters dataframes
air_quality = pd.merge(air_quality, air_quality_parameters, how='left', left_on='parameter', right_on='id')
```
