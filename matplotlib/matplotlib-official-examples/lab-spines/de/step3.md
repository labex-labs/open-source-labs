# Subplots erstellen

Wir werden drei Subplots erstellen, um verschiedene Anpassungen der Spines zu demonstrieren. Wir werden das eingeschränkte Layout verwenden, um sicherzustellen, dass die Beschriftungen nicht mit den Achsen überlappen.

```python
fig, (ax0, ax1, ax2) = plt.subplots(nrows=3, layout='constrained')
```
