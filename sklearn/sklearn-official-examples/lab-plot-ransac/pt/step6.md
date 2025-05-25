# Visualizar os resultados

Vamos plotar os dados e as linhas ajustadas do modelo linear e do regressor RANSAC.

```python
# Visualizar os resultados
lw = 2
plt.scatter(
    X[inlier_mask], y[inlier_mask], color="yellowgreen", marker=".", label="Valores interiores"
)
plt.scatter(
    X[outlier_mask], y[outlier_mask], color="gold", marker=".", label="Valores exteriores"
)
plt.plot(line_X, line_y, color="navy", linewidth=lw, label="Regressão linear")
plt.plot(
    line_X,
    line_y_ransac,
    color="cornflowerblue",
    linewidth=lw,
    label="Regressor RANSAC",
)
plt.legend(loc="lower right")
plt.xlabel("Entrada")
plt.ylabel("Resposta")
plt.show()
```
