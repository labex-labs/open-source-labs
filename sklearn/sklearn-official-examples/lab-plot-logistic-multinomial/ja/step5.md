# 1 対残りロジスティック回帰モデルの学習

ここでは、ステップ 3 と同じパラメータを使用して、1 対残りロジスティック回帰モデルを学習しますが、多クラスオプションを`"ovr"`に設定します。その後、モデルの学習スコアを表示します。

```python
clf = LogisticRegression(
        solver="sag", max_iter=100, random_state=42, multi_class="ovr"
    ).fit(X, y)

print("training score : %.3f (%s)" % (clf.score(X, y), "ovr"))
```
