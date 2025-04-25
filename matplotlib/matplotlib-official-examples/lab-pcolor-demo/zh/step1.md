# 简单的 pcolor 演示

第一步是创建一个简单的 pcolor 演示。这将向你展示如何创建一个基本的 pcolor 绘图。

```python
Z = np.random.rand(6, 10)

fig, (ax0, ax1) = plt.subplots(2, 1)

c = ax0.pcolor(Z)
ax0.set_title('默认：无边缘')

c = ax1.pcolor(Z, edgecolors='k', linewidths=4)
ax1.set_title('粗边缘')

fig.tight_layout()
plt.show()
```
