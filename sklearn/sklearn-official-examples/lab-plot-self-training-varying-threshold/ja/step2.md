# データの読み込み

```python
X, y = datasets.load_breast_cancer(return_X_y=True)
X, y = shuffle(X, y, random_state=42)
y_true = y.copy()
y[50:] = -1
total_samples = y.shape[0]
```

`breast_cancer` データセットを読み込み、シャッフルします。その後、真のラベルを `y_true` にコピーし、`y` から最初の 50 個のサンプル以外のすべてのラベルを削除します。これは、半教師あり学習のシナリオをシミュレートするために使用されます。
