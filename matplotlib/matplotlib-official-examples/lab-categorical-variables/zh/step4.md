# 散点图

我们还可以创建一个散点图来展示两个分类变量之间的关系。在这种情况下，我们将使用相同的水果数据，并给数量添加一些随机噪声以创建第二个变量。

```python
noise = np.random.rand(len(values)) * 5
plt.scatter(names, values + noise)
plt.title('Fruit Counts with Noise')
plt.xlabel('Fruit')
plt.ylabel('Count')
plt.show()
```
