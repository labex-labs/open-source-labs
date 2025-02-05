# 每隔6个误差线进行二次采样

现在，让我们应用误差线二次采样，仅绘制每隔第6个误差线。我们可以通过使用 `errorbar` 函数的 `errorevery` 参数来做到这一点。

```python
fig, ax = plt.subplots()

ax.set_title('Every 6th Errorbar')
ax.errorbar(x, y1, yerr=y1err, errorevery=6, label='y1')
ax.errorbar(x, y2, yerr=y2err, errorevery=6, label='y2')

ax.legend()
plt.show()
```
