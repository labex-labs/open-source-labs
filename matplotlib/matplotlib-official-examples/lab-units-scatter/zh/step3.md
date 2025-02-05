# 创建图表

在这一步中，我们将使用具有不同单位的掩码数组创建三个图表。

```python
# create subplots
fig, (ax1, ax2, ax3) = plt.subplots(nrows=3, sharex=True)

# plot 1
ax1.scatter(xsecs, xsecs)
ax1.yaxis.set_units(secs)

# plot 2
ax2.scatter(xsecs, xsecs, yunits=hertz)

# plot 3
ax3.scatter(xsecs, xsecs, yunits=minutes)

# set labels
ax1.set_ylabel('秒')
ax2.set_ylabel('赫兹')
ax3.set_ylabel('分钟')
ax3.set_xlabel('时间')
```
