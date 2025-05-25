# 특정 특징에 대한 부분 의존도 값 계산

```python
x_index = 0
pdp, axes = partial_dependence(model, X, features=[x_index], grid_resolution=20)

# 부분 의존도 값을 플롯합니다.
plt.plot(axes[x_index], pdp[0])
plt.xlabel(feature_names[x_index])
plt.ylabel("부분 의존도")
plt.title("부분 의존도 플롯")

plt.show()
```
