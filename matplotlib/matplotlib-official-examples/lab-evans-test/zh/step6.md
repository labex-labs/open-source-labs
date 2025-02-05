# 创建图表

在这一步中，我们将创建两个图表——一个使用自定义单位，另一个使用默认单位。

```python
fig, (ax1, ax2) = plt.subplots(1, 2)
fig.suptitle("Custom units")
fig.subplots_adjust(bottom=0.2)

# 绘制时指定单位
ax2.plot(x, y, 'o', xunits=2.0)
ax2.set_title("xunits = 2.0")
plt.setp(ax2.get_xticklabels(), rotation=30, ha='right')

# 绘制时不指定单位；将使用 axisinfo 的 None 分支
ax1.plot(x, y)  # 使用默认单位
ax1.set_title('default units')
plt.setp(ax1.get_xticklabels(), rotation=30, ha='right')

plt.show()
```
