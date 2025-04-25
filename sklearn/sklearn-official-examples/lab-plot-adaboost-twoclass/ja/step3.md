# AdaBoost による決定木を作成して適合させる

このステップでは、`sklearn.ensemble`モジュールの`AdaBoostClassifier`クラスを使って、AdaBoost による決定木を作成します。ベースの推定器として決定木を使い、`max_depth`パラメータを 1 に設定します。また、`algorithm`パラメータを"SAMME"に、`n_estimators`パラメータを 200 に設定します。最後に、分類器をデータセットに適合させます。

```python
bdt = AdaBoostClassifier(
    DecisionTreeClassifier(max_depth=1), algorithm="SAMME", n_estimators=200
)

bdt.fit(X, y)
```
