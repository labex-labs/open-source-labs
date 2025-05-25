# 랜덤 포레스트 학습 및 ROC 곡선 그리기

이 단계에서는 랜덤 포레스트 분류기를 학습하고 SVC ROC 곡선과 함께 랜덤 포레스트의 ROC 곡선을 그립니다. 이를 위해 새로운 `RandomForestClassifier` 객체를 생성하고 훈련 데이터에 맞춥니다. 그런 다음 이 분류기를 사용하여 새로운 `RocCurveDisplay` 객체를 생성합니다. 또한 동일한 축에 곡선을 그리기 위해 `ax` 매개변수를 이 함수에 전달합니다. 마지막으로 `svc_disp` 객체의 `plot()` 메서드를 호출하여 SVC ROC 곡선을 그립니다.

```python
from sklearn.ensemble import RandomForestClassifier

rfc = RandomForestClassifier(n_estimators=10, random_state=42)
rfc.fit(X_train, y_train)

ax = plt.gca()
rfc_disp = RocCurveDisplay.from_estimator(rfc, X_test, y_test, ax=ax, alpha=0.8)
svc_disp.plot(ax=ax, alpha=0.8)
plt.show()
```
