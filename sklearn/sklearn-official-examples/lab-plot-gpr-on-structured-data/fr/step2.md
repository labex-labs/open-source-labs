# Visualiser la matrice de similarité des séquences

Nous pouvons utiliser notre `SequenceKernel` pour calculer la matrice de similarité entre les séquences. Nous allons tracer cette matrice à l'aide d'une échelle de couleur, où les couleurs plus claires indiquent une plus grande similarité.

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
plt.title("Similarité des séquences sous le noyau")
plt.show()
```
