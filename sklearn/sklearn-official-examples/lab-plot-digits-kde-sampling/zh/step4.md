# 绘制结果

我们将原始数字和重新采样后的数字并排绘制在一个 4x11 的网格中。

```python
import matplotlib.pyplot as plt

# 将数据转换为 4x11 的网格
new_data = new_data.reshape((4, 11, -1))
real_data = digits.data[:44].reshape((4, 11, -1))

# 绘制真实数字和重新采样后的数字
fig, ax = plt.subplots(9, 11, subplot_kw=dict(xticks=[], yticks=[]))
for j in range(11):
    ax[4, j].set_visible(False)
    for i in range(4):
        im = ax[i, j].imshow(
            real_data[i, j].reshape((8, 8)), cmap=plt.cm.binary, interpolation="nearest"
        )
        im.set_clim(0, 16)
        im = ax[i + 5, j].imshow(
            new_data[i, j].reshape((8, 8)), cmap=plt.cm.binary, interpolation="nearest"
        )
        im.set_clim(0, 16)

ax[0, 5].set_title("从输入数据中选取")
ax[5, 5].set_title('从核密度模型中生成的"新"数字')

plt.show()
```
