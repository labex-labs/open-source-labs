# 正方形的双坐标轴

我们将创建一个带有双坐标轴的正方形坐标轴。双坐标轴会继承父坐标轴的框体纵横比。

```python
fig3, ax = plt.subplots()

ax2 = ax.twinx()

ax.plot([0, 10])
ax2.plot([12, 10])

ax.set_box_aspect(1)

plt.show()
```
