# MLE- und MCD-Mahalanobis-Distanzen vergleichen

Wir werden die Fähigkeit der auf MCD basierenden Mahalanobis-Distanzen, Ausreißer zu erkennen, hervorheben. Wir berechnen die Kubikwurzel der Mahalanobis-Distanzen, was annähernd normale Verteilungen ergibt. Anschließend stellen wir die Werte der inneren und äußeren Proben mit Boxplots dar. Die Verteilung der äußeren Proben ist für die robusten Mahalanobis-Distanzen auf der Grundlage von MCD stärker von der Verteilung der inneren Proben getrennt.

```python
fig, (ax1, ax2) = plt.subplots(1, 2)
plt.subplots_adjust(wspace=0.6)

# Berechne die Kubikwurzel der MLE-Mahalanobis-Distanzen für die Proben
emp_mahal = emp_cov.mahalanobis(X - np.mean(X, 0)) ** (0.33)
# Zeichne Boxplots
ax1.boxplot([emp_mahal[:-n_outliers], emp_mahal[-n_outliers:]], widths=0.25)
# Zeichne einzelne Proben
ax1.plot(
    np.full(n_samples - n_outliers, 1.26),
    emp_mahal[:-n_outliers],
    "+k",
    markeredgewidth=1,
)
ax1.plot(np.full(n_outliers, 2.26), emp_mahal[-n_outliers:], "+k", markeredgewidth=1)
ax1.axes.set_xticklabels(("innerer Punkt", "äußerer Punkt"), size=15)
ax1.set_ylabel(r"$\sqrt[3]{\rm{(Mahal. dist.)}}$", size=16)
ax1.set_title("Verwendung nicht-robuster Schätzungen\n(Maximum Likelihood)")

# Berechne die Kubikwurzel der MCD-Mahalanobis-Distanzen für die Proben
robust_mahal = robust_cov.mahalanobis(X - robust_cov.location_) ** (0.33)
# Zeichne Boxplots
ax2.boxplot([robust_mahal[:-n_outliers], robust_mahal[-n_outliers:]], widths=0.25)
# Zeichne einzelne Proben
ax2.plot(
    np.full(n_samples - n_outliers, 1.26),
    robust_mahal[:-n_outliers],
    "+k",
    markeredgewidth=1,
)
ax2.plot(np.full(n_outliers, 2.26), robust_mahal[-n_outliers:], "+k", markeredgewidth=1)
ax2.axes.set_xticklabels(("innerer Punkt", "äußerer Punkt"), size=15)
ax2.set_ylabel(r"$\sqrt[3]{\rm{(Mahal. dist.)}}$", size=16)
ax2.set_title("Verwendung robuster Schätzungen\n(Minimum Covariance Determinant)")

plt.show()
```
