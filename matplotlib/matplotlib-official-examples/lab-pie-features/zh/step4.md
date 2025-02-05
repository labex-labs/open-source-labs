# 为扇区添加标签

我们可以通过将标签列表传递给 `pie()` 函数的 `labels` 参数，为扇区添加标签。

```python
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct='%1.1f%%')
```
