# Конкатенация датасетов

Далее мы объединим измерения нитратов и细微颗粒物 (частиц) в одну таблицу с использованием функции `concat`.

```python
# Concatenate the two dataframes
air_quality = pd.concat([air_quality_pm25, air_quality_no2], axis=0)
```
