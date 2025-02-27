# シャッフルされたデータセットを並べ替える

numpyの `argsort()` 関数を使用して、シャッフルされたデータセットを並べ替えて、二部クラスタを連続させます。

```python
fit_data = data[np.argsort(model.row_labels_)]
fit_data = fit_data[:, np.argsort(model.column_labels_)]
```
