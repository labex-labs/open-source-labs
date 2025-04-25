# MRI 画像データを読み込む

`matplotlib`の`get_sample_data`関数を使って、サンプルの MRI 画像を読み込みます。画像は 256x256 の 16 ビット整数形式です。

```python
with cbook.get_sample_data('s1045.ima.gz') as dfile:
    im = np.frombuffer(dfile.read(), np.uint16).reshape((256, 256))
```
