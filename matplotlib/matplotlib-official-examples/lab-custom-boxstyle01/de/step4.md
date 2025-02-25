# Verwenden des benutzerdefinierten Box-Stils

Sobald Sie einen benutzerdefinierten Box-Stil implementiert und registriert haben, können Sie ihn mit `Axes.text` verwenden.

```python
fig, ax = plt.subplots(figsize=(3, 3))
ax.text(0.5, 0.5, "Test", size=30, va="center", ha="center", rotation=30,
        bbox=dict(boxstyle="angled,pad=0.5", alpha=0.2))
```
