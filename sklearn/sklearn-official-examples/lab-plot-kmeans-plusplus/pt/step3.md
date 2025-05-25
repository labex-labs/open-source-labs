# Plotar sementes iniciais ao lado dos dados de amostra

Usaremos a biblioteca matplotlib para plotar as sementes iniciais ao lado dos dados de amostra. As sementes iniciais serão mostradas como pontos azuis, e os dados de amostra serão mostrados como pontos coloridos.

```python
# Plotar sementes iniciais ao lado dos dados de amostra
plt.figure(1)
colors = ["#4EACC5", "#FF9C34", "#4E9A06", "m"]

for k, col in enumerate(colors):
    cluster_data = y_true == k
    plt.scatter(X[cluster_data, 0], X[cluster_data, 1], c=col, marker=".", s=10)

plt.scatter(centers_init[:, 0], centers_init[:, 1], c="b", s=50)
plt.title("Inicialização K-Means++")
plt.xticks([])
plt.yticks([])
plt.show()
```
