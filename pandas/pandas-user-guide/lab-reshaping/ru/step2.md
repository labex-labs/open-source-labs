# Переворачивание с помощью одиночных агрегаций

Pivot - один из ключевых методов для переформатирования данных в Pandas. Он позволяет преобразовать ваши данные, чтобы можно было их рассматривать с разных углов.

```python
# Pivot df with the mean of val0
df.pivot_table(values="val0", index="row", columns="col", aggfunc="mean", fill_value=0)
```
