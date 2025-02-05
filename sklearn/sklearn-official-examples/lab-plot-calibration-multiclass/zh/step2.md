# 拟合与校准

我们在拼接的训练集和验证集（1000个样本）上训练一个具有25个基估计器（树）的随机森林分类器。这就是未校准的分类器。

```python
from sklearn.ensemble import RandomForestClassifier

clf = RandomForestClassifier(n_estimators=25)
clf.fit(X_train_valid, y_train_valid)
```

为了训练校准后的分类器，我们从相同的随机森林分类器开始，但仅使用训练数据子集（600个样本）进行训练，然后在一个两阶段过程中，使用验证数据子集（400个样本），通过 `method='sigmoid'` 进行校准。

```python
from sklearn.calibration import CalibratedClassifierCV

clf = RandomForestClassifier(n_estimators=25)
clf.fit(X_train, y_train)
cal_clf = CalibratedClassifierCV(clf, method="sigmoid", cv="prefit")
cal_clf.fit(X_valid, y_valid)
```
