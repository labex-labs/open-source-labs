# Tracer la frontière de décision de la longueur du chemin

En définissant `response_method="decision_function"`, l'arrière-plan de `DecisionBoundaryDisplay` représente la mesure de normalité d'une observation. Un tel score est donné par la longueur du chemin moyenne sur une forêt d'arbres aléatoires, qui elle-même est donnée par la profondeur de la feuille (ou de manière équivalente le nombre de splits) nécessaire pour isoler un échantillon donné.

```python
disp = DecisionBoundaryDisplay.from_estimator(
    clf,
    X,
    response_method="decision_function",
    alpha=0.5,
)
disp.ax_.scatter(X[:, 0], X[:, 1], c=y, s=20, edgecolor="k")
disp.ax_.set_title("Frontière de décision de la longueur du chemin \nde l'IsolationForest")
plt.axis("square")
plt.legend(handles=handles, labels=["anomalies", "données normales"], title="classe réelle")
plt.colorbar(disp.ax_.collections[1])
plt.show()
```
