# 重み付きサンプルを用たグラム行列の事前計算

`precompute` オプションとサンプル重みを使ってエラスティックネットを適合させるには、まず、グラム行列を計算する前に、設計行列を中心化し、正規化された重みで再スケーリングする必要があります。設計行列を中心化するには、各行から各特徴列の重み付き平均を引きます。次に、中心化された設計行列を、対応する正規化された重みの平方根で各行を乗算することで再スケーリングします。最後に、再スケーリングされた設計行列とその転置行列の内積をとることでグラム行列を計算します。

```python
X_offset = np.average(X, axis=0, weights=normalized_weights)
X_centered = X - np.average(X, axis=0, weights=normalized_weights)
X_scaled = X_centered * np.sqrt(normalized_weights)[:, np.newaxis]
gram = np.dot(X_scaled.T, X_scaled)
```
