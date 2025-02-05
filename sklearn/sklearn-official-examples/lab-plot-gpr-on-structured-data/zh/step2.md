# 可视化序列相似性矩阵

我们可以使用我们的 `SequenceKernel` 来计算序列之间的相似性矩阵。我们将使用颜色映射来绘制这个矩阵，其中较亮的颜色表示较高的相似性。

```python
import matplotlib.pyplot as plt

X = np.array(["AGCT", "AGC", "AACT", "TAA", "AAA", "GAACA"])

kernel = SequenceKernel()
K = kernel(X)
D = kernel.diag(X)

plt.figure(figsize=(8, 5))
plt.imshow(np.diag(D**-0.5).dot(K).dot(np.diag(D**-0.5)))
plt.xticks(np.arange(len(X)), X)
plt.yticks(np.arange(len(X)), X)
plt.title("Sequence similarity under the kernel")
plt.show()
```
