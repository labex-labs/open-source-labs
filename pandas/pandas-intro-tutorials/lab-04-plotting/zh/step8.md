# 自定义并保存图表

我们可以使用Matplotlib的定制选项进一步自定义图表。我们还可以将图表保存到文件中。

```python
# 自定义并保存图表
fig, axs = plt.subplots(figsize=(12, 4))
air_quality.plot.area(ax=axs)
axs.set_ylabel("NO$_2$ concentration")
fig.savefig("no2_concentrations.png")
plt.show()
```
