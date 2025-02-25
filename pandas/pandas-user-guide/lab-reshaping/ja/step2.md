# 単一の集約を伴うピボット

ピボットは、Pandas でデータを整形するための重要な方法の 1 つです。これにより、データを変換して、さまざまな角度から見ることができます。

```python
# Pivot df with the mean of val0
df.pivot_table(values="val0", index="row", columns="col", aggfunc="mean", fill_value=0)
```
