# 将第二组数据偏移3个点

在某些情况下，我们可能希望对数据的不同部分应用误差线二次采样。我们可以通过为 `errorevery` 参数指定一个元组来实现这一点。例如，让我们对第二组数据应用误差线二次采样，但将其偏移3个数据点。

```python
fig, ax = plt.subplots()

ax.set_title('Second Series Shifted by 3')
ax.errorbar(x, y1, yerr=y1err, label='y1')
ax.errorbar(x, y2, yerr=y2err, errorevery=(3, 6), label='y2')

ax.legend()
plt.show()
```
