# 그리드 생성 및 플롯

2-단순형에서 보정되지 않은 확률의 가능한 그리드를 생성하고, 해당 확률을 보정하여 각각의 화살표를 플롯합니다. 화살표는 가장 높은 보정되지 않은 확률에 따라 색상이 지정됩니다. 이는 학습된 보정 맵을 보여줍니다.

```python
plt.figure(figsize=(10, 10))
# 확률 값의 그리드 생성
p1d = np.linspace(0, 1, 20)
p0, p1 = np.meshgrid(p1d, p1d)
p2 = 1 - p0 - p1
p = np.c_[p0.ravel(), p1.ravel(), p2.ravel()]
p = p[p[:, 2] >= 0]

# 세 클래스별 보정기를 사용하여 보정된 확률 계산
calibrated_classifier = cal_clf.calibrated_classifiers_[0]
prediction = np.vstack(
    [
        calibrator.predict(this_p)
        for calibrator, this_p in zip(calibrated_classifier.calibrators, p.T)
    ]
).T

# 보정된 예측값을 단순형 내부에 유지하도록 재정규화합니다.
# 이와 같은 재정규화 단계는 CalibratedClassifierCV 의 predict 메서드에서 다중 클래스 문제에 대해 내부적으로 수행됩니다.
prediction /= prediction.sum(axis=1)[:, None]

# 보정기가 유도하는 예측 확률의 변화를 플롯
for i in range(prediction.shape[0]):
    plt.arrow(
        p[i, 0],
        p[i, 1],
        prediction[i, 0] - p[i, 0],
        prediction[i, 1] - p[i, 1],
        head_width=1e-2,
        color=colors[np.argmax(p[i])],
    )

# 단위 단순형의 경계 플롯
plt.plot([0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0], "k", label="Simplex")

plt.grid(False)
for x in [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]:
    plt.plot([0, x], [x, 0], "k", alpha=0.2)
    plt.plot([0, 0 + (1 - x) / 2], [x, x + (1 - x) / 2], "k", alpha=0.2)
    plt.plot([x, x + (1 - x) / 2], [0, 0 + (1 - x) / 2], "k", alpha=0.2)

plt.title("학습된 sigmoid 보정 맵")
plt.xlabel("확률 클래스 1")
plt.ylabel("확률 클래스 2")
plt.xlim(-0.05, 1.05)
plt.ylim(-0.05, 1.05)

plt.show()
```
