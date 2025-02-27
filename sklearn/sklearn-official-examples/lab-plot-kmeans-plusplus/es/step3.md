# Graficar las semillas de inicialización junto con los datos de muestra

Utilizaremos la librería matplotlib para graficar las semillas de inicialización junto con los datos de muestra. Las semillas de inicialización se mostrarán como puntos azules y los datos de muestra se mostrarán como puntos coloreados.

```python
# Plot init seeds along side sample data
plt.figure(1)
colors = ["#4EACC5", "#FF9C34", "#4E9A06", "m"]

for k, col in enumerate(colors):
    cluster_data = y_true == k
    plt.scatter(X[cluster_data, 0], X[cluster_data, 1], c=col, marker=".", s=10)

plt.scatter(centers_init[:, 0], centers_init[:, 1], c="b", s=50)
plt.title("K-Means++ Initialization")
plt.xticks([])
plt.yticks([])
plt.show()
```
