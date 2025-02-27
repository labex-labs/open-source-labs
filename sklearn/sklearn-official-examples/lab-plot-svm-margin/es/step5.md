# Graficar el contorno

Graficamos el contorno de la función de decisión. Primero creamos una malla (`meshgrid`) utilizando las matrices `xx` e `yy`. Luego redimensionamos la malla en una matriz bidimensional y aplicamos el método `decision_function` de la clase `SVC` para obtener los valores predichos. Finalmente, graficamos el contorno utilizando el método `contourf`.

```python
YY, XX = np.meshgrid(yy, xx)
xy = np.vstack([XX.ravel(), YY.ravel()]).T
Z = clf.decision_function(xy).reshape(XX.shape)

plt.contourf(XX, YY, Z, cmap=plt.get_cmap("RdBu"), alpha=0.5, linestyles=["-"])

plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)

plt.xticks(())
plt.yticks(())
```
