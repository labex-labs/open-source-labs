# ボックスプロットの統計量を計算する

`matplotlib.cbook` モジュールの `boxplot_stats()` 関数は、ボックスプロットに必要な統計量を計算します。データとラベルをパラメータとして渡します。

```python
# Compute boxplot stats
stats = cbook.boxplot_stats(data, labels=labels, bootstrap=10000)
```
