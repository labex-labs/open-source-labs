# y 軸の目盛りをカスタマイズする

一番左のサブプロットの y 軸の目盛りをカスタマイズします。

```python
for irow in range(2):
    axs[irow, 0].yaxis.set_ticks(np.arange(0, 10, 2))
```
