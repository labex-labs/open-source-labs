# MNIST データセットの読み込み

scikit-learn の`fetch_openml`関数を使って MNIST データセットを読み込みます。また、`train_samples`の数を 5000 に設定することで、データのサブセットを選択します。

```python
# Turn down for faster convergence
t0 = time.time()
train_samples = 5000

# Load data from https://www.openml.org/d/554
X, y = fetch_openml(
    "mnist_784", version=1, return_X_y=True, as_frame=False, parser="pandas"
)
```
