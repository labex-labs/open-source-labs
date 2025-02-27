# 多項ロジスティック回帰モデルの学習

ここでは、scikit-learnの`LogisticRegression`関数を使って多項ロジスティック回帰モデルを学習します。ソルバーを`sag`に、最大反復回数を100に、乱数シードを42に、多クラスオプションを`"multinomial"`に設定します。その後、モデルの学習スコアを表示します。

```python
clf = LogisticRegression(
        solver="sag", max_iter=100, random_state=42, multi_class="multinomial"
    ).fit(X, y)

print("training score : %.3f (%s)" % (clf.score(X, y), "multinomial"))
```
