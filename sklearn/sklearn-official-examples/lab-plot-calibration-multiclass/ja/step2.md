# フィッティングと補正

学習用と検証用のデータ (1000 個のサンプル) を連結して、25 個のベース推定器 (木) を持つランダム フォレスト分類器を学習します。これが補正前の分類器です。

```python
from sklearn.ensemble import RandomForestClassifier

clf = RandomForestClassifier(n_estimators=25)
clf.fit(X_train_valid, y_train_valid)
```

補正済みの分類器を学習するには、同じランダム フォレスト分類器から始めて、学習用データサブセット (600 個のサンプル) のみを使用して学習し、次に 2 段階のプロセスで検証用データサブセット (400 個のサンプル) を使用して `method='sigmoid'` で補正します。

```python
from sklearn.calibration import CalibratedClassifierCV

clf = RandomForestClassifier(n_estimators=25)
clf.fit(X_train, y_train)
cal_clf = CalibratedClassifierCV(clf, method="sigmoid", cv="prefit")
cal_clf.fit(X_valid, y_valid)
```
