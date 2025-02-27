# モデルを学習する

データを分類するために GPC モデルを使用します。まず、カーネル関数を指定する必要があります。

```python
kernel = C(0.1, (1e-5, np.inf)) * DotProduct(sigma_0=0.1) ** 2
```

次に、GPC モデルを作成して、データを使って学習させます。

```python
gp = GaussianProcessClassifier(kernel=kernel)
gp.fit(X, y)
```
