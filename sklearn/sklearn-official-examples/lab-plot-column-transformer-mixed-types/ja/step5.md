# 前処理パイプラインに分類器を追加する

このステップでは、`Pipeline` を使ってロジスティック回帰分類器を前処理パイプラインに追加します。

```python
clf = Pipeline(
    steps=[("preprocessor", preprocessor), ("classifier", LogisticRegression())]
)
```
