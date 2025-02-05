# 控制大小

我们可以通过设置 `pie()` 函数的 `radius` 参数来控制饼图的大小。

```python
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct='%.0f%%',
       textprops={'size':'smaller'}, radius=0.5)
```
