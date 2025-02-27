# Построение графиков результатов эксперимента 1

Мы строим графики результатов первого эксперимента с использованием библиотек `matplotlib` и `seaborn`. Индекс Рэнда достигает максимума при `n_clusters` > `n_classes`. Другие неадаптированные меры, такие как V-мера, показывают линейную зависимость между количеством кластеров и количеством образцов. Адаптированные под случай меры, такие как ARI и AMI, демонстрируют некоторую случайную вариацию вокруг среднего значения 0.0, независимо от количества образцов и кластеров.

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
    "Clustering measures for random uniform labeling\n"
    f"against reference assignment with {n_classes} classes"
)
plt.xlabel(f"Number of clusters (Number of samples is fixed to {n_samples})")
plt.ylabel("Score value")
plt.ylim(bottom=-0.05, top=1.05)
plt.legend(plots, names, bbox_to_anchor=(0.5, 0.5))
plt.show()
```
