# Prüfe das Kompromiss zwischen erhöhter Trainingszeit und Kreuzvalidierungs-Score

```python
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(16, 6))

for ax_idx, (fit_times, test_scores, estimator) in enumerate(
    zip(
        [fit_times_nb, fit_times_svm],
        [test_scores_nb, test_scores_svm],
        [naive_bayes, svc],
    )
):
    ax[ax_idx].plot(fit_times.mean(axis=1), test_scores.mean(axis=1), "o-")
    ax[ax_idx].fill_between(
        fit_times.mean(axis=1),
        test_scores.mean(axis=1) - test_scores.std(axis=1),
        test_scores.mean(axis=1) + test_scores.std(axis=1),
        alpha=0.3,
    )
    ax[ax_idx].set_ylabel("Genauigkeit")
    ax[ax_idx].set_xlabel("Anpassungszeit (s)")
    ax[ax_idx].set_title(
        f"Leistung des {estimator.__class__.__name__} - Klassifikators"
    )

plt.show()
```
