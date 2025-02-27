# 結果をプロットする

`matplotlib.pyplot` の `matshow` を使って、元の画像と分割された画像を横並びにプロットします。

```python
import matplotlib.pyplot as plt

label_im = np.full(mask.shape, -1.0)
label_im[mask] = labels

fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))
axs[0].matshow(img)
axs[1].matshow(label_im)

plt.show()
```
