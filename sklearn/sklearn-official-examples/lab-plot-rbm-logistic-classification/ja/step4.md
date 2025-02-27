# 評価

このステップでは、テストデータセット上でモデルの性能を評価します。`sklearn.metrics` モジュールの `classification_report` 関数を使用して、パイプラインモデルとロジスティック回帰モデルの両方に対する分類レポートを生成します。

```python
from sklearn import metrics

Y_pred = rbm_features_classifier.predict(X_test)
print(
    "Logistic regression using RBM features:\n%s\n"
    % (metrics.classification_report(Y_test, Y_pred))
)

# 画素値を直接使ってロジスティック回帰分類器を学習させる
raw_pixel_classifier = clone(logistic)
raw_pixel_classifier.C = 100.0
raw_pixel_classifier.fit(X_train, Y_train)

Y_pred = raw_pixel_classifier.predict(X_test)
print(
    "Logistic regression using raw pixel features:\n%s\n"
    % (metrics.classification_report(Y_test, Y_pred))
)
```
