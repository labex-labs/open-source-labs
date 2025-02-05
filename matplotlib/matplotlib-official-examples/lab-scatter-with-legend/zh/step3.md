# 自动创建图例

我们还可以使用 `PathCollection.legend_elements` 方法为散点图自动创建图例。此方法将尝试确定要显示的有用数量的图例条目，并返回句柄和标签的元组。

```python
N = 45
x, y = np.random.rand(2, N)
c = np.random.randint(1, 5, size=N)
s = np.random.randint(10, 220, size=N)

fig, ax = plt.subplots()

scatter = ax.scatter(x, y, c=c, s=s)

# 从散点图中使用唯一颜色生成一个图例
legend1 = ax.legend(*scatter.legend_elements(),
                    loc="lower left", title="Classes")
ax.add_artist(legend1)

# 从散点图中使用大小的一个横截面生成一个图例
handles, labels = scatter.legend_elements(prop="sizes", alpha=0.6)
legend2 = ax.legend(handles, labels, loc="upper right", title="Sizes")

plt.show()
```
