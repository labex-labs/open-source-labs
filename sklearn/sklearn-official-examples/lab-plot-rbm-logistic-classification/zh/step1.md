# 数据准备

在这一步中，我们准备用于训练和测试的数据。我们使用`sklearn.datasets`中的`load_digits`函数来获取数据集。然后，我们通过在每个方向上对训练数据进行 1 像素的线性偏移来人为地生成更多带标签的数据。我们将数据缩放到 0 到 1 之间。

```python
import numpy as np
from scipy.ndimage import convolve
from sklearn import datasets
from sklearn.preprocessing import minmax_scale
from sklearn.model_selection import train_test_split

def nudge_dataset(X, Y):
    """
    此函数通过将 X 中的 8x8 图像向左、右、下、上移动 1 像素，生成一个比原始数据集大 5 倍的数据集
    """
    direction_vectors = [
        [[0, 1, 0], [0, 0, 0], [0, 0, 0]],
        [[0, 0, 0], [1, 0, 0], [0, 0, 0]],
        [[0, 0, 0], [0, 0, 1], [0, 0, 0]],
        [[0, 0, 0], [0, 0, 0], [0, 1, 0]],
    ]

    def shift(x, w):
        return convolve(x.reshape((8, 8)), mode="constant", weights=w).ravel()

    X = np.concatenate(
        [X] + [np.apply_along_axis(shift, 1, X, vector) for vector in direction_vectors]
    )
    Y = np.concatenate([Y for _ in range(5)], axis=0)
    return X, Y

X, y = datasets.load_digits(return_X_y=True)
X = np.asarray(X, "float32")
X, Y = nudge_dataset(X, y)
X = minmax_scale(X, feature_range=(0, 1))  # 0-1 缩放

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=0)
```
