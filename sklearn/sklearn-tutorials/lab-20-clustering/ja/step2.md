# サンプルデータを生成する

次に、使用するサンプルデータを生成しましょう。`sklearn.datasets` モジュールの `make_blobs` 関数を使って、クラスタがある合成データセットを作成します。

```python
# Generate sample data
X, y = make_blobs(n_samples=100, centers=4, random_state=0, cluster_std=1.0)
```
