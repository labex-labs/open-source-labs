# Plotar Contorno

Plotamos o contorno da função de decisão. Primeiro, criamos uma malha usando os arrays `xx` e `yy`. Em seguida, transformamos a malha em um array 2D e aplicamos o método `decision_function` da classe `SVC` para obter os valores previstos. Em seguida, plotamos o contorno usando o método `contourf`.

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
