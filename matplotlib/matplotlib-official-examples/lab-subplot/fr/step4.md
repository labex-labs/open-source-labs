# Définir le titre et les étiquettes des axes

Nous allons définir le titre et les étiquettes des axes pour nos sous-graphiques.

```python
# Définir le titre et les étiquettes des axes
fig.suptitle('A tale of 2 subplots')

ax1.set_ylabel('Oscillation amortie')
ax2.set_xlabel('temps (s)')
ax2.set_ylabel('Non amortie')
```
