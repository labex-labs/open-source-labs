# 绘制正则化路径

我们将使用训练模型的系数来绘制正则化路径。系数将相对于正则化强度的对数进行绘制。在图的左侧（强正则化器），所有系数都恰好为 0。当正则化逐渐变宽松时，系数会相继变为非零值。

```python
import matplotlib.pyplot as plt

plt.plot(np.log10(cs), coefs_, marker="o")
ymin, ymax = plt.ylim()
plt.xlabel("log(C)")
plt.ylabel("Coefficients")
plt.title("Logistic Regression Path")
plt.axis("tight")
plt.show()
```
