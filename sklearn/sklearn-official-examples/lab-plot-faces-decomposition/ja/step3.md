# 非負成分 - NMF

次に、非負行列分解（NMF）を適用します。これは、データ行列を 2 つの非負行列に分解します。1 つは基底ベクトルを含み、もう 1 つは係数を含みます。これにより、データの部分ベースの表現が得られます。

```python
# 非負成分 - NMF
nmf_estimator = decomposition.NMF(n_components=n_components, tol=5e-3)
nmf_estimator.fit(faces)  # 元の非負データセット
plot_gallery("Non-negative components - NMF", nmf_estimator.components_[:n_components])
```
