# データにノイズを追加する

次に、numpyを使ってデータポイント間の対距離にノイズを追加します。

```python
similarities = euclidean_distances(X_true)

# 類似度にノイズを追加する
noise = np.random.rand(n_samples, n_samples)
noise = noise + noise.T
noise[np.arange(noise.shape[0]), np.arange(noise.shape[0])] = 0
similarities += noise
```
