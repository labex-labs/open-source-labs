# Kreuztabulationen

Die Kreuztabulation ist eine Methode, um das Verhältnis zwischen mehreren Variablen quantitativ zu analysieren.

```python
# Kreuztabulation zwischen row und col
df.pivot_table(index="row", columns="col", fill_value=0, aggfunc="size")
```
