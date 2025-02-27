# データの読み込み

次に、Scikit-learn の `fetch_openml` 関数を使用して MNIST データセットを読み込みます。

```python
X, y = fetch_openml(
    "mnist_784", version=1, return_X_y=True, as_frame=False, parser="pandas"
)
```
