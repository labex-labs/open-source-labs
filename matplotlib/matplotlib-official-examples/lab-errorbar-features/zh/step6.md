# 绘制带误差线的对数刻度图

最后，我们将绘制带有对数刻度和误差线的数据图。`ax.set_yscale()`函数用于将y轴设置为对数刻度。

```python
# 绘制带误差线的对数刻度图
fig, ax = plt.subplots()
ax.errorbar(x, y, yerr=error, fmt='o')
ax.set_title('Log Scale with Error Bars')
ax.set_yscale('log')
plt.show()
```
