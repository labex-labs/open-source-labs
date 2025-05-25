# 다항 특징 보간

`PolynomialFeatures`를 사용하여 다항 특징을 생성하고 릿지 회귀 모델을 학습 데이터에 맞춥니다. 그런 다음 다항 특징을 사용하여 함수, 학습 점 및 보간 결과를 플롯합니다.

```python
# 함수 플롯
lw = 2
fig, ax = plt.subplots()
ax.set_prop_cycle(
    color=["black", "teal", "yellowgreen", "gold", "darkorange", "tomato"]
)
ax.plot(x_plot, f(x_plot), linewidth=lw, label="ground truth")

# 학습 점 플롯
ax.scatter(x_train, y_train, label="training points")

# 다항 특징
for degree in [3, 4, 5]:
    model = make_pipeline(PolynomialFeatures(degree), Ridge(alpha=1e-3))
    model.fit(X_train, y_train)
    y_plot = model.predict(X_plot)
    ax.plot(x_plot, y_plot, label=f"degree {degree}")

ax.legend(loc="lower center")
ax.set_ylim(-20, 10)
plt.show()
```
