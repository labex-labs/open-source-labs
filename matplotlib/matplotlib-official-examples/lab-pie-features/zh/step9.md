# 修改阴影

我们可以通过将一个参数字典传递给 `pie()` 函数的 `shadow` 参数来修改饼图的阴影。

```python
fig, ax = plt.subplots()
ax.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
       shadow={'ox': -0.04, 'edgecolor': 'none','shade': 0.9}, startangle=90)
```
