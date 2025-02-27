# モデルを作成する

次に、`sklearn.cluster` モジュールの `AgglomerativeClustering()` 関数を使って階層的クラスタリングモデルを作成します。

```python
model = AgglomerativeClustering(distance_threshold=0, n_clusters=None)
```
