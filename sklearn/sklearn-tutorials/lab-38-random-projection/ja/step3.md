# ガウス型ランダム射影

次に、データの次元を削減するためにガウス型ランダム射影を適用しましょう。

```python
transformer = random_projection.GaussianRandomProjection()
X_new = transformer.fit_transform(X)
```

このステップでは、`GaussianRandomProjection` クラスのインスタンスを作成し、データ `X` に適合させます。その後、`fit_transform` メソッドを呼び出すことで変換を適用します。結果は `X_new` 変数に格納されます。
