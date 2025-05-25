# ROC 곡선 생성

ROC 곡선을 그리려면 추정기에서 확률 또는 임계값이 적용되지 않은 결정 값이 필요합니다. 로지스틱 회귀는 결정 함수를 제공하므로 이를 사용하여 ROC 곡선을 그립니다.

```python
from sklearn.metrics import roc_curve
from sklearn.metrics import RocCurveDisplay

y_score = clf.decision_function(X_test)

fpr, tpr, _ = roc_curve(y_test, y_score, pos_label=clf.classes_[1])
roc_display = RocCurveDisplay(fpr=fpr, tpr=tpr).plot()
```
