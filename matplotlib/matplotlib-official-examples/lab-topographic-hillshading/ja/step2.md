# データを読み込む

次に、Matplotlib の`get_sample_data`関数を使ってサンプルの標高データを読み込みます。そして、標高データとグリッドのセルサイズを抽出します。

```python
dem = get_sample_data('jacksboro_fault_dem.npz')
z = dem['elevation']
dx, dy = dem['dx'], dem['dy']
```
