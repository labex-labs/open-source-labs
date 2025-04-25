# 多項ロジスティック回帰モデルの学習

ここでは、scikit-learn の`LogisticRegression`関数を使って多項ロジスティック回帰モデルを学習します。ソルバーを`sag`に、最大反復回数を 100 に、乱数シードを 42 に、多クラスオプションを`"multinomial"`に設定します。その後、モデルの学習スコアを表示します。

```python
clf = LogisticRegression(
        solver="sag", max_iter=100, random_state=42, multi_class="multinomial"
    ).fit(X, y)

print("training score : %.3f (%s)" % (clf.score(X, y), "multinomial"))
```
