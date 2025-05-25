# Plotar os limites de decisão e os pontos de treino

Neste passo, plotaremos os limites de decisão e os pontos de treino. Criaremos um objeto `DecisionBoundaryDisplay` utilizando o método `from_estimator` do módulo `sklearn.inspection` e passaremos o classificador AdaBoost, o conjunto de dados e outros parâmetros. Também plotaremos os pontos de treino utilizando cores diferentes para cada classe.

```python
plot_colors = "br"
plot_step = 0.02
class_names = "AB"

plt.figure(figsize=(10, 5))

# Plotar os limites de decisão
ax = plt.subplot(121)
disp = DecisionBoundaryDisplay.from_estimator(
    bdt,
    X,
    cmap=plt.cm.Paired,
    response_method="predict",
    ax=ax,
    xlabel="x",
    ylabel="y",
)
x_min, x_max = disp.xx0.min(), disp.xx0.max()
y_min, y_max = disp.xx1.min(), disp.xx1.max()
plt.axis("tight")

# Plotar os pontos de treino
for i, n, c in zip(range(2), class_names, plot_colors):
    idx = np.where(y == i)
    plt.scatter(
        X[idx, 0],
        X[idx, 1],
        c=c,
        cmap=plt.cm.Paired,
        s=20,
        edgecolor="k",
        label="Classe %s" % n,
    )
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.legend(loc="upper right")

plt.title("Limite de Decisão")
```
