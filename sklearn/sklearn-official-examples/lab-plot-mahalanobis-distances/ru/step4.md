# Сравнение расстояний Махаланобиса MLE и MCD

Мы выявим способность расстояний Махаланобиса, основанных на MCD, различать выбросы. Мы берем кубический корень из расстояний Махаланобиса, получая приблизительно нормальные распределения. Затем мы строим значения для выборок с внутренними и внешними точками с использованием ящиковых диаграмм. Распределение выборок с выбросами более отделено от распределения выборок с внутренними точками для расстояний Махаланобиса, основанных на устойчивом MCD.

```python
fig, (ax1, ax2) = plt.subplots(1, 2)
plt.subplots_adjust(wspace=0.6)

# Вычисление кубического корня расстояний Махаланобиса MLE для выборок
emp_mahal = emp_cov.mahalanobis(X - np.mean(X, 0)) ** (0.33)
# Построение ящиковых диаграмм
ax1.boxplot([emp_mahal[:-n_outliers], emp_mahal[-n_outliers:]], widths=0.25)
# Построение отдельных выборок
ax1.plot(
    np.full(n_samples - n_outliers, 1.26),
    emp_mahal[:-n_outliers],
    "+k",
    markeredgewidth=1,
)
ax1.plot(np.full(n_outliers, 2.26), emp_mahal[-n_outliers:], "+k", markeredgewidth=1)
ax1.axes.set_xticklabels(("inliers", "outliers"), size=15)
ax1.set_ylabel(r"$\sqrt[3]{\rm{(Mahal. dist.)}}$", size=16)
ax1.set_title("Using non-robust estimates\n(Maximum Likelihood)")

# Вычисление кубического корня расстояний Махаланобиса MCD для выборок
robust_mahal = robust_cov.mahalanobis(X - robust_cov.location_) ** (0.33)
# Построение ящиковых диаграмм
ax2.boxplot([robust_mahal[:-n_outliers], robust_mahal[-n_outliers:]], widths=0.25)
# Построение отдельных выборок
ax2.plot(
    np.full(n_samples - n_outliers, 1.26),
    robust_mahal[:-n_outliers],
    "+k",
    markeredgewidth=1,
)
ax2.plot(np.full(n_outliers, 2.26), robust_mahal[-n_outliers:], "+k", markeredgewidth=1)
ax2.axes.set_xticklabels(("inliers", "outliers"), size=15)
ax2.set_ylabel(r"$\sqrt[3]{\rm{(Mahal. dist.)}}$", size=16)
ax2.set_title("Using robust estimates\n(Minimum Covariance Determinant)")

plt.show()
```
