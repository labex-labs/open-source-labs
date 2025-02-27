# パイプラインの評価

ここでは、`predict` メソッドを使ってテスト用サブセット上でパイプラインを評価します。パイプラインは ANOVA F 値に基づいて最も情報量の多い 3 つの特徴を選択し、`LinearSVC` 関数は選択された特徴に基づいて予測を行います。

```python
from sklearn.metrics import classification_report

y_pred = anova_svm.predict(X_test)
print(classification_report(y_test, y_pred))
```
