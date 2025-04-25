# VotingClassifier の初期化

次に、重み付け `[1, 1, 5]` を持つソフト投票の VotingClassifier を初期化します。これは、平均確率を計算する際に、RandomForestClassifier の予測確率が他の分類器の重みの 5 倍の重みを持つことを意味します。

```python
eclf = VotingClassifier(
    estimators=[("lr", clf1), ("rf", clf2), ("gnb", clf3)],
    voting="soft",
    weights=[1, 1, 5],
)
```
