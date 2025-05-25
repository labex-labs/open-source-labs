# Visualizar Dados

Antes de aplicar o algoritmo K-Means Clustering, vamos primeiro visualizar os dados para melhor compreendê-los. Usaremos um gráfico de dispersão 3D para visualizar os dados.

```python
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection="3d")
ax.scatter(X[:, 0], X[:, 1], X[:, 2])
ax.set_xlabel("Comprimento da sépala")
ax.set_ylabel("Largura da sépala")
ax.set_zlabel("Comprimento da pétala")
plt.show()
```
