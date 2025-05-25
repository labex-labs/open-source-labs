# 교정 곡선 플롯

작은 학습 데이터셋으로 네 가지 모델 각각을 학습하고 테스트 데이터셋의 예측 확률을 사용하여 교정 곡선을 플롯합니다. 교정 곡선은 예측 확률을 구간으로 나누고 각 구간의 평균 예측 확률을 관측된 빈도 ('양성 비율') 와 함께 플롯하여 생성합니다. 교정 곡선 아래에는 예측 확률의 분포를 보여주는 히스토그램 (보다 구체적으로 각 예측 확률 구간의 샘플 수) 이 플롯됩니다.

```python
import numpy as np
from sklearn.svm import LinearSVC
from sklearn.calibration import CalibrationDisplay
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

# 분류기 생성
lr = LogisticRegression()
gnb = GaussianNB()
svc = NaivelyCalibratedLinearSVC(C=1.0, dual="auto")
rfc = RandomForestClassifier()

clf_list = [
    (lr, "Logistic"),
    (gnb, "Naive Bayes"),
    (svc, "SVC"),
    (rfc, "Random forest"),
]

fig = plt.figure(figsize=(10, 10))
gs = GridSpec(4, 2)
colors = plt.get_cmap("Dark2")

ax_calibration_curve = fig.add_subplot(gs[:2, :2])
calibration_displays = {}
markers = ["^", "v", "s", "o"]
for i, (clf, name) in enumerate(clf_list):
    clf.fit(X_train, y_train)
    display = CalibrationDisplay.from_estimator(
        clf,
        X_test,
        y_test,
        n_bins=10,
        name=name,
        ax=ax_calibration_curve,
        color=colors(i),
        marker=markers[i],
    )
    calibration_displays[name] = display

ax_calibration_curve.grid()
ax_calibration_curve.set_title("Calibration plots")

# 히스토그램 추가
grid_positions = [(2, 0), (2, 1), (3, 0), (3, 1)]
for i, (_, name) in enumerate(clf_list):
    row, col = grid_positions[i]
    ax = fig.add_subplot(gs[row, col])

    ax.hist(
        calibration_displays[name].y_prob,
        range=(0, 1),
        bins=10,
        label=name,
        color=colors(i),
    )
    ax.set(title=name, xlabel="평균 예측 확률", ylabel="개수")

plt.tight_layout()
plt.show()
```
