# 加载 MRI 数据并显示图像

第一步是加载 MRI 数据并显示图像。我们将使用 `imshow()` 函数来显示图像，并使用 `axis('off')` 来移除坐标轴标签。

```python
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure("MRI_with_EEG")

# 加载 MRI 数据（256x256 16 位整数）
im = np.load('mri_data.npy')

# 绘制 MRI 图像
ax0 = fig.add_subplot(2, 2, 1)
ax0.imshow(im, cmap='gray')
ax0.axis('off')
```
