# 保存绘图

我们可以使用 `savefig` 函数将绘图保存为图像文件。

```python
fig, ax = plt.subplots()
for shape in shapes:
    ax.add_artist(shape)
plt.xlim([-0.5, 1.5])
plt.ylim([-0.5, 1.5])
plt.axis('off')
plt.savefig('shapes.png')
```
