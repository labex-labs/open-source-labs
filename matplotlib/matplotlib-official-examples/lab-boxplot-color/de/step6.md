# Hinzufügen horizontaler Gitternetzlinien

Schließlich werden wir horizontalen Gitternetzlinien zu den Boxplots mit der `yaxis.grid()`-Funktion hinzufügen.

```python
for ax in [ax1, ax2]:
    ax.yaxis.grid(True)
    ax.set_xlabel('Drei separate Proben')
    ax.set_ylabel('Beobachtete Werte')

plt.show()
```
