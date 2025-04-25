# k-means++ からシードを計算する

scikit-learn ライブラリの`kmeans_plusplus`関数を使って、k-means++ からシードを計算します。この関数は、k-means クラスタリングに使用される初期クラスタ中心を返します。k-means++ を使って 4 つのクラスタを計算します。

```python
# Calculate seeds from k-means++
centers_init, indices = kmeans_plusplus(X, n_clusters=4, random_state=0)
```
