#Comparer les temps d'ajustement avec et sans arrêt précoce

Nous allons maintenant comparer les temps d'ajustement des deux modèles.

```python
plt.figure(figsize=(9, 5))

bar1 = plt.bar(
    index, time_gb, bar_width, label="Sans arrêt précoce", color="crimson"
)
bar2 = plt.bar(
    index + bar_width, time_gbes, bar_width, label="Avec arrêt précoce", color="coral"
)

max_y = np.amax(np.maximum(time_gb, time_gbes))

plt.xticks(index + bar_width, names)
plt.yticks(np.linspace(0, 1.3 * max_y, 13))

autolabel(bar1, n_gb)
autolabel(bar2, n_gbes)

plt.ylim([0, 1.3 * max_y])
plt.legend(loc="best")
plt.grid(True)

plt.xlabel("Ensembles de données")
plt.ylabel("Temps d'ajustement")

plt.show()
```
