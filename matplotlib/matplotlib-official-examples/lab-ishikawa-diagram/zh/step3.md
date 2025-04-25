# 创建鱼骨图

现在我们将创建鱼骨图。我们将首先创建一个图形和轴对象。

```python
fig, ax = plt.subplots(figsize=(10, 6), layout='constrained')
```

接下来，我们将设置轴的 x 和 y 限制，并关闭轴。

```python
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.axis('off')
```
