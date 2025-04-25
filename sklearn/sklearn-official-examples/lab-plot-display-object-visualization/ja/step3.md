# RocCurveDisplay の作成

ROC 曲線には、推定器からの確率または閾値なしの判定値が必要です。ロジスティック回帰は判定関数を提供するため、ROC 曲線を描画するためにそれを使用します。

```python
from sklearn.metrics import roc_curve
from sklearn.metrics import RocCurveDisplay

y_score = clf.decision_function(X_test)

fpr, tpr, _ = roc_curve(y_test, y_score, pos_label=clf.classes_[1])
roc_display = RocCurveDisplay(fpr=fpr, tpr=tpr).plot()
```
