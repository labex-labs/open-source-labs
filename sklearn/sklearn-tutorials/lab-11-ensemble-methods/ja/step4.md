# バギング分類器 (Bagging Classifier) の適合

ここでは、訓練データにバギング分類器 (Bagging Classifier) を適合させます。バギング分類器は、ブートストラップサンプリングを使用して複数のベースモデル（多くの場合、決定木）を作成し、多数決によってそれらの予測を集約するアンサンブル法です。

```python
bagging = BaggingClassifier(DecisionTreeClassifier(), n_estimators=10)
bagging.fit(X_train, y_train)
```
