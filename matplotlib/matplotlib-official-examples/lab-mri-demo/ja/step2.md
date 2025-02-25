# MRI画像データを読み込む

`matplotlib`の`get_sample_data`関数を使って、サンプルのMRI画像を読み込みます。画像は256x256の16ビット整数形式です。

```python
with cbook.get_sample_data('s1045.ima.gz') as dfile:
    im = np.frombuffer(dfile.read(), np.uint16).reshape((256, 256))
```
