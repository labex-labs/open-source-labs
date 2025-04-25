# 重塑数据

有时，数据最初可能不是 scikit-learn 所需的形状。在这种情况下，我们需要对数据进行预处理，将其转换为`(n_samples, n_features)`形状。重塑数据的一个例子是手写数字数据集，它由 1797 个 8x8 的手写数字图像组成：

```python
digits = datasets.load_digits()
print(digits.images.shape)
```

输出：

```
(1797, 8, 8)
```

为了在 scikit-learn 中使用这个数据集，我们需要将每个 8x8 的图像重塑为长度为 64 的特征向量：

```python
data = digits.images.reshape((digits.images.shape[0], -1))
```
