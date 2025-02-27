# ランダムデータに対する順列検定スコア

次に、ランダムに生成された特徴量とアヤメのラベルを使用して `permutation_test_score` を計算します。これらの特徴量とラベルの間には依存関係がないはずです。

```python
score_rand, perm_scores_rand, pvalue_rand = permutation_test_score(
    clf, X_rand, y, scoring="accuracy", cv=cv, n_permutations=1000
)
```
