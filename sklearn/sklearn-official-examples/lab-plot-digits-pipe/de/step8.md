# Zeichnen der Klassifikationsgenauigkeit

Wir werden die Klassifikationsgenauigkeit für jede Anzahl von Komponenten zeichnen.

```python
best_clfs.plot(
    x=components_col, y="mean_test_score", yerr="std_test_score", legend=False, ax=ax1
)
ax1.set_ylabel("Klassifikationsgenauigkeit (val)")
ax1.set_xlabel("n_components")

plt.xlim(-1, 70)

plt.tight_layout()
plt.show()
```
