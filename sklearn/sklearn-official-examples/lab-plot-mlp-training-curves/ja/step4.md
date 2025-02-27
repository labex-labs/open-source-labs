# 小さなデータセットを読み込むまたは生成する

ここで、この例で使用する小さなデータセットを読み込むか生成する必要があります。アヤメデータセット (iris dataset)、手書き数字データセット (digits dataset)、および `make_circles` と `make_moons` 関数を使用して生成される 2 つのデータセットを使用します。

```python
iris = datasets.load_iris()
X_digits, y_digits = datasets.load_digits(return_X_y=True)
data_sets = [
    (iris.data, iris.target),
    (X_digits, y_digits),
    datasets.make_circles(noise=0.2, factor=0.5, random_state=1),
    datasets.make_moons(noise=0.3, random_state=0),
]
```
