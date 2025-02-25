# グラフとサブプロットを作成する

データを表示するためにグラフとサブプロットを作成する必要があります。この実験では、横並びに 2 つのサブプロットを作成します。

```python
# Figure width is doubled (2*6.4) to display nicely 2 subplots side by side.
fig, (ax0, ax1) = plt.subplots(nrows=2, figsize=(7, 9.6))
for ax in (ax0, ax1):
    ax.set_xscale('log')
```
