# Ergebnisse plotten

Wir werden das matplotlib.pyplot-Modul verwenden, um die Ergebnisse zu plotten. Kerndatenpunkte (große Punkte) und Nicht-Kerndatenpunkte (kleine Punkte) werden entsprechend dem zugewiesenen Cluster farblich kodiert. Datenpunkte, die als Rausch markiert sind, werden in Schwarz dargestellt.

```python
unique_labels = set(labels)
core_samples_mask = np.zeros_like(labels, dtype=bool)
core_samples_mask[db.core_sample_indices_] = True

colors = [plt.cm.Spectral(each) for each in np.linspace(0, 1, len(unique_labels))]
for k, col in zip(unique_labels, colors):
    if k == -1:
        col = [0, 0, 0, 1]

    class_member_mask = labels == k

    xy = X[class_member_mask & core_samples_mask]
    plt.plot(
        xy[:, 0],
        xy[:, 1],
        "o",
        markerfacecolor=tuple(col),
        markeredgecolor="k",
        markersize=14,
    )

    xy = X[class_member_mask & ~core_samples_mask]
    plt.plot(
        xy[:, 0],
        xy[:, 1],
        "o",
        markerfacecolor=tuple(col),
        markeredgecolor="k",
        markersize=6,
    )

plt.title(f"Geschätzte Anzahl der Cluster: {n_clusters_}")
plt.show()
```
