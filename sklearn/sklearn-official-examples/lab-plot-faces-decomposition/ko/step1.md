# 데이터 준비

먼저 Olivetti 얼굴 데이터 세트를 로드하고 전처리합니다. 데이터를 전역적으로 (하나의 특징에 집중하여 모든 샘플을 중심화) 및 지역적으로 (하나의 샘플에 집중하여 모든 특징을 중심화) 0 평균을 갖도록 중심화합니다. 또한 얼굴 갤러리를 플롯하는 기본 함수를 정의합니다.

```python
# Olivetti 얼굴 데이터 세트를 로드하고 전처리합니다.

import logging

from numpy.random import RandomState
import matplotlib.pyplot as plt

from sklearn.datasets import fetch_olivetti_faces
from sklearn import cluster
from sklearn import decomposition

rng = RandomState(0)

# 표준 출력에 진행 로그 표시
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

faces, _ = fetch_olivetti_faces(return_X_y=True, shuffle=True, random_state=rng)
n_samples, n_features = faces.shape

# 전역 중심화 (하나의 특징에 집중하여 모든 샘플을 중심화)
faces_centered = faces - faces.mean(axis=0)

# 지역 중심화 (하나의 샘플에 집중하여 모든 특징을 중심화)
faces_centered -= faces_centered.mean(axis=1).reshape(n_samples, -1)

print("데이터 세트는 %d개의 얼굴로 구성됩니다" % n_samples)

# 얼굴 갤러리를 플롯하는 기본 함수를 정의합니다.

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


# 데이터를 살펴봅니다. 회색은 음수 값, 흰색은 양수 값을 나타냅니다.

plot_gallery("데이터 세트의 얼굴", faces_centered[:n_components])
```
