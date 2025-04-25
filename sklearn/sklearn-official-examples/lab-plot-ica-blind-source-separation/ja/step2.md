# ICA と PCA モデルの適合

独立成分を推定するために FastICA を使います。その後、比較のために PCA を計算します。

```python
from sklearn.decomposition import FastICA, PCA

# ICA を計算する
ica = FastICA(n_components=3, whiten="arbitrary-variance")
S_ = ica.fit_transform(X)  # 信号を再構築する
A_ = ica.mixing_  # 推定された混合行列を取得する

# アンミキシングを元に戻すことで ICA モデルが適用されることを「証明」できます。
assert np.allclose(X, np.dot(S_, A_.T) + ica.mean_)

# 比較のために、PCA を計算する
pca = PCA(n_components=3)
H = pca.fit_transform(X)  # 直交成分に基づいて信号を再構築する
```
