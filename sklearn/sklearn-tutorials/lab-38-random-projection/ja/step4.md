# 疎ランダム射影

次に、疎ランダム射影と呼ばれる別の種類のランダム射影を試してみましょう。

```python
transformer = random_projection.SparseRandomProjection()
X_new = transformer.fit_transform(X)
```

ここでは、`SparseRandomProjection` クラスのインスタンスを作成し、`fit_transform` メソッドを使ってデータ `X` に適用します。結果は `X_new` 変数に格納されます。
