# MRI データの読み込みと画像の表示

最初のステップは、MRI データを読み込み、画像を表示することです。画像を表示するには`imshow()`関数を、軸のラベルを削除するには`axis('off')`を使用します。

```python
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure("MRI_with_EEG")

# MRI データを読み込む (256x256 の 16 ビット整数)
im = np.load('mri_data.npy')

# MRI 画像をプロットする
ax0 = fig.add_subplot(2, 2, 1)
ax0.imshow(im, cmap='gray')
ax0.axis('off')
```
