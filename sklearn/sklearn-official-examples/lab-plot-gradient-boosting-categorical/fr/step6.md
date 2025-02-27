# Comparaison des modèles

Nous allons comparer les performances des quatre pipelines en utilisant la validation croisée et tracer les temps d'ajustement et les scores d'erreur moyenne en pourcentage absolue.

```python
from sklearn.model_selection import cross_validate
import matplotlib.pyplot as plt

scoring = "neg_mean_absolute_percentage_error"
n_cv_folds = 3

dropped_result = cross_validate(hist_dropped, X, y, cv=n_cv_folds, scoring=scoring)
one_hot_result = cross_validate(hist_one_hot, X, y, cv=n_cv_folds, scoring=scoring)
ordinal_result = cross_validate(hist_ordinal, X, y, cv=n_cv_folds, scoring=scoring)
native_result = cross_validate(hist_native, X, y, cv=n_cv_folds, scoring=scoring)

def plot_results(figure_title):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 8))

    plot_info = [
        ("fit_time", "Temps d'ajustement (s)", ax1, None),
        ("test_score", "Erreur moyenne en pourcentage absolue", ax2, None),
    ]

    x, width = np.arange(4), 0.9
    for key, title, ax, y_limit in plot_info:
        items = [
            dropped_result[key],
            one_hot_result[key],
            ordinal_result[key],
            native_result[key],
        ]

        mape_cv_mean = [np.mean(np.abs(item)) for item in items]
        mape_cv_std = [np.std(item) for item in items]

        ax.bar(
            x=x,
            height=mape_cv_mean,
            width=width,
            yerr=mape_cv_std,
            color=["C0", "C1", "C2", "C3"],
        )
        ax.set(
            xlabel="Modèle",
            title=title,
            xticks=x,
            xticklabels=["Supprimé", "One Hot", "Ordinal", "Natif"],
            ylim=y_limit,
        )
    fig.suptitle(figure_title)

plot_results("Gradient Boosting sur le logement d'Ames")
```
