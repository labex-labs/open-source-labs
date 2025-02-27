# k-means++からシードを計算する

scikit-learnライブラリの`kmeans_plusplus`関数を使って、k-means++からシードを計算します。この関数は、k-meansクラスタリングに使用される初期クラスタ中心を返します。k-means++を使って4つのクラスタを計算します。

```python
# Calculate seeds from k-means++
centers_init, indices = kmeans_plusplus(X, n_clusters=4, random_state=0)
```
