# Visualizar Dados

Usaremos o Matplotlib para visualizar os conjuntos de dados gerados. No bloco de código a seguir, criamos um gráfico 2x2 mostrando os clusters verdadeiros para cada conjunto de dados.

```python
import matplotlib.pyplot as plt

fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(12, 12))

axs[0, 0].scatter(X[:, 0], X[:, 1], c=y)
axs[0, 0].set_title("Mistura de Blobs Gaussianos")

axs[0, 1].scatter(X_aniso[:, 0], X_aniso[:, 1], c=y)
axs[0, 1].set_title("Blobs Distribuídos Anisotropicamente")

axs[1, 0].scatter(X_varied[:, 0], X_varied[:, 1], c=y_varied)
axs[1, 0].set_title("Variância Desigual")

axs[1, 1].scatter(X_filtered[:, 0], X_filtered[:, 1], c=y_filtered)
axs[1, 1].set_title("Blobs com Tamanhos Desiguais")

plt.suptitle("Clusters verdadeiros").set_y(0.95)
plt.show()
```
