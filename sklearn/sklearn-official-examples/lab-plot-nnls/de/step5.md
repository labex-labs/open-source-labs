# Regressionskoeffizienten vergleichen

Wir werden nun die Regressionskoeffizienten zwischen der nichtnegativen kleinsten Quadrate Regression und der klassischen linearen Regression vergleichen. Wir werden die Koeffizienten gegeneinander aufzeichnen und feststellen, dass sie stark korreliert sind. Allerdings schrumpft die nichtnegative Einschränkung einige Koeffizienten auf 0. Dies liegt daran, dass die nichtnegative kleinste Quadrate von Natur aus dünne Ergebnisse liefern.

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.plot(reg_ols.coef_, reg_nnls.coef_, linewidth=0, marker=".")

low_x, high_x = ax.get_xlim()
low_y, high_y = ax.get_ylim()
low = max(low_x, low_y)
high = min(high_x, high_y)
ax.plot([low, high], [low, high], ls="--", c=".3", alpha=0.5)
ax.set_xlabel("OLS regression coefficients", fontweight="bold")
ax.set_ylabel("NNLS regression coefficients", fontweight="bold")
```
