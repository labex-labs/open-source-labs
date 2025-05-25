# Visualizar Matriz de Similaridade de Sequências

Podemos usar nosso `SequenceKernel` para calcular a matriz de similaridade entre sequências. Iremos plotar esta matriz usando uma escala de cores, onde cores mais brilhantes indicam maior similaridade.

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
plt.title("Similaridade de sequências sob o kernel")
plt.show()
```
