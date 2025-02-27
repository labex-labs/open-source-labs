# Traçage des résultats de l'expérience 1

Nous traçons les résultats de la première expérience en utilisant les bibliothèques `matplotlib` et `seaborn`. L'indice de Rand atteint un plateau pour `n_clusters` > `n_classes`. D'autres mesures non ajustées telles que la mesure V montrent une dépendance linéaire entre le nombre de groupes et le nombre d'échantillons. Les mesures ajustées pour le hasard, telles que l'ARI et l'AMI, présentent quelques variations aléatoires centrées autour d'une valeur moyenne de 0,0, indépendamment du nombre d'échantillons et de groupes.

```python
import matplotlib.pyplot as plt
import seaborn as sns

n_samples = 1000
n_classes = 10
n_clusters_range = np.linspace(2, 100, 10).astype(int)
plots = []
names = []

sns.color_palette("colorblind")
plt.figure(1)

for marker, (score_name, score_func) in zip("d^vx.,", score_funcs):
    scores = fixed_classes_uniform_labelings_scores(
        score_func, n_samples, n_clusters_range, n_classes=n_classes
    )
    plots.append(
        plt.errorbar(
            n_clusters_range,
            scores.mean(axis=1),
            scores.std(axis=1),
            alpha=0.8,
            linewidth=1,
            marker=marker,
        )[0]
    )
    names.append(score_name)

plt.title(
    "Mesures de regroupement pour un étiquetage uniforme aléatoire\n"
    f"par rapport à une affectation de référence avec {n_classes} classes"
)
plt.xlabel(f"Nombre de groupes (Le nombre d'échantillons est fixé à {n_samples})")
plt.ylabel("Valeur du score")
plt.ylim(bottom=-0.05, top=1.05)
plt.legend(plots, names, bbox_to_anchor=(0.5, 0.5))
plt.show()
```
