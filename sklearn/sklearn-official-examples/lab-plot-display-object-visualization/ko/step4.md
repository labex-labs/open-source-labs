# Precision-Recall 곡선 생성

마찬가지로, 이전 섹션의 `y_score`를 사용하여 정밀도 - 재현율 곡선을 그릴 수 있습니다.

```python
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import PrecisionRecallDisplay

prec, recall, _ = precision_recall_curve(y_test, y_score, pos_label=clf.classes_[1])
pr_display = PrecisionRecallDisplay(precision=prec, recall=recall).plot()
```
