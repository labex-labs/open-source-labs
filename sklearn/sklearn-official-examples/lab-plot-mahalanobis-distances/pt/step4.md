# Comparar Distâncias de Mahalanobis MLE e MCD

Destacaremos a capacidade das distâncias de Mahalanobis baseadas em MCD de distinguir valores discrepantes. Tomamos a raiz cúbica das distâncias de Mahalanobis, obtendo distribuições aproximadamente normais. Em seguida, plotamos os valores das amostras internas e externas com diagramas de caixa. A distribuição das amostras externas está mais separada da distribuição das amostras internas para as distâncias de Mahalanobis baseadas em MCD robustas.

```python
fig, (ax1, ax2) = plt.subplots(1, 2)
plt.subplots_adjust(wspace=0.6)

# Calcular a raiz cúbica das distâncias de Mahalanobis MLE para as amostras
emp_mahal = emp_cov.mahalanobis(X - np.mean(X, 0)) ** (0.33)
# Plotar diagramas de caixa
ax1.boxplot([emp_mahal[:-n_outliers], emp_mahal[-n_outliers:]], widths=0.25)
# Plotar amostras individuais
ax1.plot(
    np.full(n_samples - n_outliers, 1.26),
    emp_mahal[:-n_outliers],
    "+k",
    markeredgewidth=1,
)
ax1.plot(np.full(n_outliers, 2.26), emp_mahal[-n_outliers:], "+k", markeredgewidth=1)
ax1.axes.set_xticklabels(("inliers", "outliers"), size=15)
ax1.set_ylabel(r"$\sqrt[3]{\rm{(Mahal. dist.)}}$", size=16)
ax1.set_title("Utilizando estimativas não robustas\n(Máxima Verossimilhança)")

# Calcular a raiz cúbica das distâncias de Mahalanobis MCD para as amostras
robust_mahal = robust_cov.mahalanobis(X - robust_cov.location_) ** (0.33)
# Plotar diagramas de caixa
ax2.boxplot([robust_mahal[:-n_outliers], robust_mahal[-n_outliers:]], widths=0.25)
# Plotar amostras individuais
ax2.plot(
    np.full(n_samples - n_outliers, 1.26),
    robust_mahal[:-n_outliers],
    "+k",
    markeredgewidth=1,
)
ax2.plot(np.full(n_outliers, 2.26), robust_mahal[-n_outliers:], "+k", markeredgewidth=1)
ax2.axes.set_xticklabels(("inliers", "outliers"), size=15)
ax2.set_ylabel(r"$\sqrt[3]{\rm{(Mahal. dist.)}}$", size=16)
ax2.set_title("Utilizando estimativas robustas\n(Determinante Mínimo de Covariância)")

plt.show()
```
