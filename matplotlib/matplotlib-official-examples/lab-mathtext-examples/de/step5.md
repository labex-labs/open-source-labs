# Die Formel der Kopfzeiledemonstration plotten

In diesem Schritt werden wir die Formel der Kopfzeiledemonstration plotten.

```python
full_demo = mathtext_demos['Header demo']
ax.annotate(full_demo,
            xy=(0.5, 1. - 0.59 * line_axesfrac),
            color='tab:orange', ha='center', fontsize=20)
```
