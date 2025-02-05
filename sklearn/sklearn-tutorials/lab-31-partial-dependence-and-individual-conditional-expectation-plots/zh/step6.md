# 计算特定特征的部分依赖值

```python
x_index = 0
pdp, axes = partial_dependence(model, X, features=[x_index], grid_resolution=20)

# 绘制部分依赖值
plt.plot(axes[x_index], pdp[0])
plt.xlabel(feature_names[x_index])
plt.ylabel("部分依赖")
plt.title("部分依赖图")

plt.show()
```
