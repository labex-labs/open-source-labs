# Visualisiere die Sequenzähnlichkeitsmatrix

Wir können unseren `SequenceKernel` verwenden, um die Ähnlichkeitsmatrix zwischen Sequenzen zu berechnen. Wir werden diese Matrix mit einer Farbskala plotten, wobei hellere Farben eine höhere Ähnlichkeit anzeigen.

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
