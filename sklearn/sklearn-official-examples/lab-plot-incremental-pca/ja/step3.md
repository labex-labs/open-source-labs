# IPCA を実行する

IPCA クラスのインスタンスを初期化し、データに適合させることで、Iris データセットに対して IPCA を実行します。

```python
n_components = 2
ipca = IncrementalPCA(n_components=n_components, batch_size=10)
X_ipca = ipca.fit_transform(X)
```
