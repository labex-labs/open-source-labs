# 결정 경계 및 학습 데이터 시각화

이 단계에서는 결정 경계와 학습 데이터 포인트를 시각화합니다. `sklearn.inspection` 모듈의 `from_estimator` 메서드를 사용하여 `DecisionBoundaryDisplay` 객체를 생성하고, AdaBoost 분류기, 데이터셋 및 다른 매개변수를 전달합니다. 각 클래스에 대해 다른 색상을 사용하여 학습 데이터 포인트를 플롯합니다.

```python
plot_colors = "br"
plot_step = 0.02
class_names = "AB"

plt.figure(figsize=(10, 5))

# 결정 경계 플롯
ax = plt.subplot(121)
disp = DecisionBoundaryDisplay.from_estimator(
    bdt,
    X,
    cmap=plt.cm.Paired,
    response_method="predict",
    ax=ax,
    xlabel="x",
    ylabel="y",
)
x_min, x_max = disp.xx0.min(), disp.xx0.max()
y_min, y_max = disp.xx1.min(), disp.xx1.max()
plt.axis("tight")

# 학습 데이터 포인트 플롯
for i, n, c in zip(range(2), class_names, plot_colors):
    idx = np.where(y == i)
    plt.scatter(
        X[idx, 0],
        X[idx, 1],
        c=c,
        cmap=plt.cm.Paired,
        s=20,
        edgecolor="k",
        label="Class %s" % n,
    )
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.legend(loc="upper right")

plt.title("Decision Boundary")
```
