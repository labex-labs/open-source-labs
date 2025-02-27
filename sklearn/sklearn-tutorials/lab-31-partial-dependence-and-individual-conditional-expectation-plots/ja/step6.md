# 特定の特徴量に対する部分依存性の値を計算する

```python
x_index = 0
pdp, axes = partial_dependence(model, X, features=[x_index], grid_resolution=20)

# 部分依存性の値をプロットする
plt.plot(axes[x_index], pdp[0])
plt.xlabel(feature_names[x_index])
plt.ylabel("Partial Dependence")
plt.title("Partial Dependence Plot")

plt.show()
```
