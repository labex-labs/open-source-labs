# スペクトラルコクラスタリングを実行する

次に、スペクトラルコクラスタリングアルゴリズムを使用してバイクラスタリングを実行しましょう。このアルゴリズムは、他の行と列と比較して値の高いバイクラスタを見つけます。

```python
# Initialize and fit the Spectral Co-Clustering model
model_co = SpectralCoclustering(n_clusters=3, random_state=0)
model_co.fit(data)

# Get row and column cluster membership
row_clusters_co = model_co.row_labels_
column_clusters_co = model_co.column_labels_
```
