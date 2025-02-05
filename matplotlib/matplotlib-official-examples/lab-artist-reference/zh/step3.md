# 绘制形状

现在，我们将通过遍历 `shapes` 列表并将它们添加到绘图中来使用 Matplotlib 绘制形状。

```python
fig, ax = plt.subplots()
for shape in shapes:
    ax.add_artist(shape)
plt.xlim([-0.5, 1.5])
plt.ylim([-0.5, 1.5])
plt.axis('off')
plt.show()
```
