# 数据集准备

首先，我们加载并预处理 Olivetti 人脸数据集。我们对数据进行中心化处理，使均值为零，包括全局中心化（关注一个特征，将所有样本中心化）和局部中心化（关注一个样本，将所有特征中心化）。我们还定义了一个基础函数来绘制人脸图像集。

```python
# 加载并预处理 Olivetti 人脸数据集。

import logging

from numpy.random import RandomState
import matplotlib.pyplot as plt

from sklearn.datasets import fetch_olivetti_faces
from sklearn import cluster
from sklearn import decomposition

rng = RandomState(0)

# 在标准输出上显示进度日志
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

faces, _ = fetch_olivetti_faces(return_X_y=True, shuffle=True, random_state=rng)
n_samples, n_features = faces.shape

# 全局中心化（关注一个特征，将所有样本中心化）
faces_centered = faces - faces.mean(axis=0)

# 局部中心化（关注一个样本，将所有特征中心化）
faces_centered -= faces_centered.mean(axis=1).reshape(n_samples, -1)

print("数据集包含 %d 张人脸" % n_samples)

# 定义一个基础函数来绘制人脸图像集。

n_row, n_col = 2, 3
n_components = n_row * n_col
image_shape = (64, 64)


def plot_gallery(title, images, n_col=n_col, n_row=n_row, cmap=plt.cm.gray):
    fig, axs = plt.subplots(
        nrows=n_row,
        ncols=n_col,
        figsize=(2.0 * n_col, 2.3 * n_row),
        facecolor="white",
        constrained_layout=True,
    )
    fig.set_constrained_layout_pads(w_pad=0.01, h_pad=0.02, hspace=0, wspace=0)
    fig.set_edgecolor("black")
    fig.suptitle(title, size=16)
    for ax, vec in zip(axs.flat, images):
        vmax = max(vec.max(), -vec.min())
        im = ax.imshow(
            vec.reshape(image_shape),
            cmap=cmap,
            interpolation="nearest",
            vmin=-vmax,
            vmax=vmax,
        )
        ax.axis("off")

    fig.colorbar(im, ax=axs, orientation="horizontal", shrink=0.99, aspect=40, pad=0.01)
    plt.show()


# 让我们看看我们的数据。灰色表示负值，
# 白色表示正值。

plot_gallery("数据集中的人脸", faces_centered[:n_components])
```
