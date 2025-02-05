# 自定义图例元素

我们可以通过在 `PathCollection.legend_elements` 方法中使用其他参数来进一步自定义图例元素。例如，我们可以指定要创建的图例条目的数量以及它们应该如何标注。

```python
volume = np.random.rayleigh(27, size=40)
amount = np.random.poisson(10, size=40)
ranking = np.random.normal(size=40)
price = np.random.uniform(1, 10, size=40)

fig, ax = plt.subplots()

# 因为当将价格作为 `s` 的大小提供时，价格太小了，
# 所以我们将其归一化为一些有用的点大小，s = 0.3 * (价格 * 3) ** 2
scatter = ax.scatter(volume, amount, c=ranking, s=0.3 * (price * 3) ** 2,
                     vmin=-3, vmax=3, cmap="Spectral")

# 为排名（颜色）生成一个图例。即使有40种不同的排名，
# 我们只想在图例中显示其中的5种。
legend1 = ax.legend(*scatter.legend_elements(num=5),
                    loc="upper left", title="Ranking")
ax.add_artist(legend1)

# 为价格（大小）生成一个图例。因为我们想用美元显示价格，
# 所以我们使用 *func* 参数来提供用于从上面计算大小的函数的反函数。
# *fmt* 确保以美元显示价格。请注意，我们这里目标是5个元素，
# 但由于为我们自动选择的舍入价格，在创建的图例中只得到了4个。
kw = dict(prop="sizes", num=5, color=scatter.cmap(0.7), fmt="$ {x:.2f}",
          func=lambda s: np.sqrt(s/.3)/3)
legend2 = ax.legend(*scatter.legend_elements(**kw),
                    loc="lower right", title="Price")

plt.show()
```
