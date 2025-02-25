# データの読み込み

次に、このチュートリアルで使用するサンプルデータを読み込みます。標高データが含まれる `jacksboro_fault_dem.npz` ファイルを使用します。

```python
dem = cbook.get_sample_data('jacksboro_fault_dem.npz')
elev = dem['elevation']
```
