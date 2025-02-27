#Comparer les scores avec et sans arrêt précoce

Nous allons maintenant comparer les scores des deux modèles.

```python
plt.figure(figsize=(9, 5))

bar1 = plt.bar(
    index, score_gb, bar_width, label="Sans arrêt précoce", color="crimson"
)
bar2 = plt.bar(
    index + bar_width, score_gbes, bar_width, label="Avec arrêt précoce", color="coral"
)

plt.xticks(index + bar_width, names)
plt.yticks(np.arange(0, 1.3, 0.1))

autolabel(bar1, n_gb)
autolabel(bar2, n_gbes)

plt.ylim([0, 1.3])
plt.legend(loc="best")
plt.grid(True)

plt.xlabel("Ensembles de données")
plt.ylabel("Score de test")

plt.show()
```
