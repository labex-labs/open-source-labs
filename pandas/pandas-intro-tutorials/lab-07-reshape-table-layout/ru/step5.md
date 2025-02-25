# Преобразование данных из широкого формата в длинный

Теперь преобразуем данные о 𝑁𝑂2 в широком формате в длинный формат с использованием функции `melt`.

```python
# Сброс индекса для no2_pivoted
no2_pivoted = no2.pivot(columns="location", values="value").reset_index()

# Преобразование данных
no_2 = no2_pivoted.melt(id_vars="date.utc")
```
