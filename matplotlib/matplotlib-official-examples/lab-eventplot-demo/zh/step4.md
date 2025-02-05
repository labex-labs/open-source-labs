# 创建第一个事件图 - 水平方向

我们将创建第一个水平方向的事件图。

```python
fig, axs = plt.subplots(2, 2)

axs[0, 0].eventplot(data1, colors=colors1, lineoffsets=lineoffsets1,
                    linelengths=linelengths1)
```
