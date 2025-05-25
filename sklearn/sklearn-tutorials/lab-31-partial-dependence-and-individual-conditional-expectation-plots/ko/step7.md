# 특정 특징에 대한 개별 조건부 기댓값 계산

```python
x_index = 0
ice, axes = partial_dependence(model, X, features=[x_index], kind='individual')

# 개별 조건부 기댓값을 플롯합니다.
for i in range(len(ice)):
    plt.plot(axes[x_index], ice[i], color='lightgray')
plt.plot(axes[x_index], np.mean(ice, axis=0), color='blue')
plt.xlabel(feature_names[x_index])
plt.ylabel("개별 조건부 기댓값")
plt.title("개별 조건부 기댓값 플롯")

plt.show()
```
