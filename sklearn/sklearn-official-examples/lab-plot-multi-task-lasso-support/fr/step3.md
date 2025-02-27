# Tracer les résultats

Enfin, nous pouvons tracer les résultats de nos modèles pour voir comment ils se comparent. Nous tracerons le support (c'est-à-dire l'emplacement des coefficients non nuls) pour chaque modèle, ainsi que la série temporelle d'une des caractéristiques.

```python
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(8, 5))
plt.subplot(1, 2, 1)
plt.spy(coef_lasso_)
plt.xlabel("Caractéristique")
plt.ylabel("Temps (ou Tâche)")
plt.text(10, 5, "Lasso")
plt.subplot(1, 2, 2)
plt.spy(coef_multi_task_lasso_)
plt.xlabel("Caractéristique")
plt.ylabel("Temps (ou Tâche)")
plt.text(10, 5, "MultiTaskLasso")
fig.suptitle("Emplacement des coefficients non nuls")

feature_to_plot = 0
plt.figure()
lw = 2
plt.plot(coef[:, feature_to_plot], color="seagreen", linewidth=lw, label="Vérité terrain")
plt.plot(
    coef_lasso_[:, feature_to_plot], color="cornflowerblue", linewidth=lw, label="Lasso"
)
plt.plot(
    coef_multi_task_lasso_[:, feature_to_plot],
    color="gold",
    linewidth=lw,
    label="MultiTaskLasso",
)
plt.legend(loc="upper center")
plt.axis("tight")
plt.ylim([-1.1, 1.1])
plt.show()
```
