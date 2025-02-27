# パイプラインの学習

ここでは、`fit` メソッドを使って訓練用サブセット上でパイプラインを学習します。学習中に、`SelectKBest` 関数は ANOVA F 値に基づいて最も情報量の多い 3 つの特徴を選択し、`LinearSVC` 関数は選択された特徴に基づいて線形 SVM 分類器を学習します。

```python
anova_svm.fit(X_train, y_train)
```
