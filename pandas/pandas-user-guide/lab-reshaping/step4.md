# Cross Tabulations

Cross tabulation is a method to quantitatively analyze the relationship between multiple variables.

```python
# Cross tabulation between row and col
df.pivot_table(index="row", columns="col", fill_value=0, aggfunc="size")
```
