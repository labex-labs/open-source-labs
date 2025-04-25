# モデルの学習

2 つの SVM モデルを作成します。最初のモデルはサンプル重みを考慮せず、2 番目のモデルは先ほど作成したサンプル重みを考慮します。

```python
clf_no_weights = svm.SVC(gamma=1)
clf_no_weights.fit(X, y)

clf_weights = svm.SVC(gamma=1)
clf_weights.fit(X, y, sample_weight=sample_weight_last_ten)
```
