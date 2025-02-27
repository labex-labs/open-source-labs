# 特定の特徴量に対する個別条件期待値を計算する

```python
x_index = 0
ice, axes = partial_dependence(model, X, features=[x_index], kind='individual')

# 個別条件期待値をプロットする
for i in range(len(ice)):
    plt.plot(axes[x_index], ice[i], color='lightgray')
plt.plot(axes[x_index], np.mean(ice, axis=0), color='blue')
plt.xlabel(feature_names[x_index])
plt.ylabel("Individual Conditional Expectation")
plt.title("Individual Conditional Expectation Plot")

plt.show()
```
