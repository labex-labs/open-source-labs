# Построить точность классификации

Мы построим точность классификации для каждого количества компонентов.

```python
best_clfs.plot(
    x=components_col, y="mean_test_score", yerr="std_test_score", legend=False, ax=ax1
)
ax1.set_ylabel("Точность классификации (валидация)")
ax1.set_xlabel("n_components")

plt.xlim(-1, 70)

plt.tight_layout()
plt.show()
```
