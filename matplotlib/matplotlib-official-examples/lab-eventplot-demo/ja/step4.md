# 最初のイベントプロットを作成する - 水平方向

水平方向の最初のイベントプロットを作成します。

```python
fig, axs = plt.subplots(2, 2)

axs[0, 0].eventplot(data1, colors=colors1, lineoffsets=lineoffsets1,
                    linelengths=linelengths1)
```
