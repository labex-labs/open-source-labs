# 分离扇区

我们可以通过将一个值列表传递给 `pie()` 函数的 `explode` 参数，来分离饼图中的一个或多个扇区。

```python
explode = (0, 0.1, 0, 0)  # 仅分离第二个扇区（即 'Hogs'）

fig, ax = plt.subplots()
ax.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
       shadow=True, startangle=90)
```
