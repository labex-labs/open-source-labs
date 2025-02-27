# Visualiser les résultats

Enfin, nous allons visualiser les résultats des modèles entraînés à l'aide d'un graphique en ligne.

```python
fig = plt.figure()
ax = fig.add_subplot(111)

for model in models:
    name = models[model]["name"]
    times = models[model]["times"]
    accuracies = models[model]["accuracies"]
    ax.plot(times, accuracies, marker="o", label="Modèle : %s" % name)
    ax.set_xlabel("Temps d'entraînement (s)")
    ax.set_ylabel("Précision de test")
ax.legend()
fig.suptitle("Multinomiale vs One-vs-Rest Logistique L1\nEnsemble de données %s" % "20newsgroups")
fig.tight_layout()
fig.subplots_adjust(top=0.85)
run_time = timeit.default_timer() - t0
print("Exécution de l'exemple en %.3f s" % run_time)
plt.show()
```
