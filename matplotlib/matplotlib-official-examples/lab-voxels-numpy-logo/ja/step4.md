# ボクセル画像を拡大する

ここでは、先ほど定義した`explode`関数を使って、ボクセル画像を拡大し、各ボクセルの間に隙間を残します。

```python
filled = np.ones(n_voxels.shape)
filled_2 = explode(filled)
fcolors_2 = explode(facecolors)
ecolors_2 = explode(edgecolors)
```
