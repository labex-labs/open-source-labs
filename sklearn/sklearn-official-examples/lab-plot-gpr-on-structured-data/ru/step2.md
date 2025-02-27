# Визуализация матрицы сходства последовательностей

Мы можем использовать наш `SequenceKernel` для вычисления матрицы сходства между последовательностями. Мы построим эту матрицу с использованием цветовой карты, где более яркие цвета указывают на более высокую сходство.

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
