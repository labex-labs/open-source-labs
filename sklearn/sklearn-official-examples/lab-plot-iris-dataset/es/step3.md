# Visualizar los datos

Visualizaremos el Conjunto de Datos Iris utilizando un diagrama de dispersión. Graficaremos la Longitud del Sépalo contra el Ancho del Sépalo y colorearemos los puntos según su clase.

```python
x_min, x_max = X[:, 0].min() - 0.5, X[:, 0].max() + 0.5
y_min, y_max = X[:, 1].min() - 0.5, X[:, 1].max() + 0.5

plt.figure(2, figsize=(8, 6))
plt.clf()

# Plot the training points
plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Set1, edgecolor="k")
plt.xlabel("Longitud del Sépalo")
plt.ylabel("Ancho del Sépalo")

plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.xticks(())
plt.yticks(())
```
