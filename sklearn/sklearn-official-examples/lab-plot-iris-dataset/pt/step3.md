# Visualizar os Dados

Visualizaremos o Conjunto de Dados Iris usando um gráfico de dispersão. Plotaremos a Comprimento da Sépala contra a Largura da Sépala, e coloriremos os pontos com base em sua classe.

```python
x_min, x_max = X[:, 0].min() - 0.5, X[:, 0].max() + 0.5
y_min, y_max = X[:, 1].min() - 0.5, X[:, 1].max() + 0.5

plt.figure(2, figsize=(8, 6))
plt.clf()

# Plotar os pontos de treinamento
plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Set1, edgecolor="k")
plt.xlabel("Comprimento da Sépala")
plt.ylabel("Largura da Sépala")

plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.xticks(())
plt.yticks(())
```
