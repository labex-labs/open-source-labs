# B-스플라인 보간

`SplineTransformer`를 사용하여 B-스플라인 기저 함수를 생성하고 릿지 회귀 모델을 학습 데이터에 맞춥니다. 그런 다음 B-스플라인을 사용하여 함수, 학습 점 및 보간 결과를 플롯합니다.

```python
# 4 + 3 - 1 = 6 개의 기저 함수를 갖는 B-스플라인
model = make_pipeline(SplineTransformer(n_knots=4, degree=3), Ridge(alpha=1e-3))
model.fit(X_train, y_train)

y_plot = model.predict(X_plot)
ax.plot(x_plot, y_plot, label="B-spline")
ax.legend(loc="lower center")
ax.set_ylim(-20, 10)
plt.show()
```
