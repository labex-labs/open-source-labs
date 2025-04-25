# アンサンブル分類器を定義する

`max_features`パラメータに異なる値を持つ 3 つのランダムフォレスト分類器のリストを定義します。訓練中の OOB エラー率の追跡を可能にするために、`warm_start`構築パラメータを`True`に設定します。また、OOB エラー率の計算を可能にするために、`oob_score`パラメータを`True`に設定します。

```python
ensemble_clfs = [
    (
        "RandomForestClassifier, max_features='sqrt'",
        RandomForestClassifier(
            warm_start=True,
            oob_score=True,
            max_features="sqrt",
            random_state=RANDOM_STATE,
        ),
    ),
    (
        "RandomForestClassifier, max_features='log2'",
        RandomForestClassifier(
            warm_start=True,
            max_features="log2",
            oob_score=True,
            random_state=RANDOM_STATE,
        ),
    ),
    (
        "RandomForestClassifier, max_features=None",
        RandomForestClassifier(
            warm_start=True,
            max_features=None,
            oob_score=True,
            random_state=RANDOM_STATE,
        ),
    ),
]
```
