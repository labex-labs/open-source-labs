# データセットの生成

scikit-learn の`make_blobs`関数を使用して、3 クラスのデータセットを生成します。1000 個のサンプルを使用し、ブロブの中心を`[-5, 0], [0, 1.5], [5, -1]`に設定します。その後、データセットを変換行列を使って変換して、分類がより難しくなるようにします。

```python
centers = [[-5, 0], [0, 1.5], [5, -1]]
X, y = make_blobs(n_samples=1000, centers=centers, random_state=40)
transformation = [[0.4, 0.2], [-0.4, 1.2]]
X = np.dot(X, transformation)
```
