# スペクトラル共クラスタリングアルゴリズムを適用する

5 つのクラスタに対して、シャッフルされたデータセットにスペクトラル共クラスタリングアルゴリズムを適用します。

```python
model = SpectralCoclustering(n_clusters=5, random_state=0)
model.fit(data)
```
