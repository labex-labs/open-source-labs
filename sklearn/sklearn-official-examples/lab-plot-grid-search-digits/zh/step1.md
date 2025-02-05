# 加载数据

我们将加载数字数据集并将图像展平为向量。每个 8x8 像素的图像都需要转换为一个 64 像素的向量。因此，我们将得到一个形状为 `(n_images, n_pixels)` 的最终数据数组。我们还将把数据分成大小相等的训练集和测试集。

```python
from sklearn import datasets
from sklearn.model_selection import train_test_split

digits = datasets.load_digits()

n_samples = len(digits.images)
X = digits.images.reshape((n_samples, -1))
y = digits.target == 8

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=0)
```
