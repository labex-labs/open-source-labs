# Создание сводной таблицы

Создайте сводную таблицу, чтобы найти средние концентрации для 𝑁𝑂2 и 𝑃𝑀25 в каждом из станций.

```python
air_quality.pivot_table(
    values="value", index="location", columns="parameter", aggfunc="mean"
)
```
