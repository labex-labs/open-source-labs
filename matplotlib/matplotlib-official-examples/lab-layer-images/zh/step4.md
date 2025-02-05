# 创建第二张图像

使用`func3`函数和`imshow`函数创建第二张图像。

```python
Z2 = func3(X, Y)
im2 = plt.imshow(Z2, cmap=plt.cm.viridis, alpha=.9, interpolation='bilinear',
                 extent=extent)
```
