# PrecisionRecallDisplay の作成

同様に、前節の `y_score` を使用して適合率再現率曲線を描画することができます。

```python
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import PrecisionRecallDisplay

prec, recall, _ = precision_recall_curve(y_test, y_score, pos_label=clf.classes_[1])
pr_display = PrecisionRecallDisplay(precision=prec, recall=recall).plot()
```
