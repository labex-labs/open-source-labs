# ROC 및 DET 곡선 플롯

scikit-learn 의 `RocCurveDisplay` 및 `DetCurveDisplay` 클래스를 사용하여 각각 ROC 및 DET 곡선을 플롯합니다. `RocCurveDisplay.from_estimator` 함수는 ROC 곡선을 계산하고 지정된 축에 플롯합니다. 마찬가지로 `DetCurveDisplay.from_estimator` 함수는 DET 곡선을 계산하고 지정된 축에 플롯합니다. ROC 곡선용 하나와 DET 곡선용 하나의 두 개의 서브플롯을 생성하고 각 분류기의 곡선을 플롯합니다.

```python
import matplotlib.pyplot as plt
from sklearn.metrics import DetCurveDisplay, RocCurveDisplay

fig, [ax_roc, ax_det] = plt.subplots(1, 2, figsize=(11, 5))

for name, clf in classifiers.items():
    clf.fit(X_train, y_train)

    RocCurveDisplay.from_estimator(clf, X_test, y_test, ax=ax_roc, name=name)
    DetCurveDisplay.from_estimator(clf, X_test, y_test, ax=ax_det, name=name)

ax_roc.set_title("수신자 작동 특성 (ROC) 곡선")
ax_det.set_title("검출 오류 트레이드오프 (DET) 곡선")

ax_roc.grid(linestyle="--")
ax_det.grid(linestyle="--")

plt.legend()
plt.show()
```
