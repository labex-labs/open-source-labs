# 计算特定特征的个体条件期望值

```python
x_index = 0
ice, axes = partial_dependence(model, X, features=[x_index], kind='individual')

# 绘制个体条件期望值
for i in range(len(ice)):
    plt.plot(axes[x_index], ice[i], color='lightgray')
plt.plot(axes[x_index], np.mean(ice, axis=0), color='blue')
plt.xlabel(feature_names[x_index])
plt.ylabel("个体条件期望")
plt.title("个体条件期望图")

plt.show()
```
