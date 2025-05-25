# Plotar o Hiperplano de Separação de Margem Máxima

Para plotar o hiperplano de separação de margem máxima, utilizaremos a função `DecisionBoundaryDisplay.from_estimator()` do scikit-learn. Esta função plota a função de decisão e os vetores de suporte do classificador SVM. Também plotaremos os vetores de suporte como círculos sem preenchimento e com borda preta.

```python
from sklearn.inspection import DecisionBoundaryDisplay

# plotar a função de decisão e os vetores de suporte
ax = plt.gca()
DecisionBoundaryDisplay.from_estimator(
    clf,
    X,
    plot_method="contour",
    colors="k",
    levels=[-1, 0, 1],
    alpha=0.5,
    linestyles=["--", "-", "--"],
    ax=ax,
)
ax.scatter(
    clf.support_vectors_[:, 0],
    clf.support_vectors_[:, 1],
    s=100,
    linewidth=1,
    facecolors="none",
    edgecolors="k",
)
plt.show()
```
