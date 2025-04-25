# 设置主刻度定位器和次刻度定位器

```python
# 设置主刻度定位器
ax.xaxis.set_major_locator(MultipleLocator(20))
# 设置主刻度格式化器
ax.xaxis.set_major_formatter('{x:.0f}')
# 设置次刻度定位器
ax.xaxis.set_minor_locator(MultipleLocator(5))
```

在这里，我们将主刻度定位器设置为以 20 的倍数放置刻度，将主刻度格式化器设置为使用".0f"格式标注主刻度，并将次刻度定位器设置为以 5 的倍数放置刻度。
