# 创建并可视化个体条件期望图

```python
fig, ax = plot_partial_dependence(model, X, features=[(0, 1), (2, 3)], feature_names=feature_names, kind='individual')

# 设置图形大小和标题
fig.set_size_inches(10, 8)
fig.suptitle('个体条件期望图')

plt.show()
```
