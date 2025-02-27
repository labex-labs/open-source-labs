# 検証

逆変換の正確性を検証するために、元のデータ `X` と逆変換の結果を比較することができます。

```python
X_new_again = transformer.transform(X_new_inversed)
np.allclose(X_new, X_new_again)
```

ここでは、逆変換されたデータ `X_new_inversed` に変換を適用し、`np.allclose` 関数を使ってそれが元の射影データ `X_new` と等しいかどうかを確認します。
