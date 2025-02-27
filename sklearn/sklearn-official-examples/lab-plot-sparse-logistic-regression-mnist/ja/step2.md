# MNISTデータセットの読み込み

scikit-learnの`fetch_openml`関数を使ってMNISTデータセットを読み込みます。また、`train_samples`の数を5000に設定することで、データのサブセットを選択します。

```python
# Turn down for faster convergence
t0 = time.time()
train_samples = 5000

# Load data from https://www.openml.org/d/554
X, y = fetch_openml(
    "mnist_784", version=1, return_X_y=True, as_frame=False, parser="pandas"
)
```
