# 绘制所有误差线

接下来，我们将使用 `errorbar` 函数绘制所有误差线，不进行任何二次采样。这将作为我们的基线图。

```python
fig, ax = plt.subplots()

ax.set_title('All Errorbars')
ax.errorbar(x, y1, yerr=y1err, label='y1')
ax.errorbar(x, y2, yerr=y2err, label='y2')

ax.legend()
plt.show()
```
