# 加载数据集

在这一步中，我们将从scikit-learn中加载数字数据集。该数据集包含0到9的手写数字图像。

```python
digits = datasets.load_digits()
images = digits.images
X = np.reshape(images, (len(images), -1))
```
