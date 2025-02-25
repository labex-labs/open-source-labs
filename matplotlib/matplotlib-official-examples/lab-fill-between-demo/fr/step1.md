# Utilisation de base

La fonction `fill_between` peut être utilisée pour remplir la zone entre deux lignes. Les paramètres `y1` et `y2` peuvent être des scalaires, indiquant une limite horizontale aux valeurs de y données. Si seul `y1` est donné, `y2` est égal à 0 par défaut.

```python
x = np.arange(0.0, 2, 0.01)
y1 = np.sin(2 * np.pi * x)
y2 = 0.8 * np.sin(4 * np.pi * x)

fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True, figsize=(6, 6))

ax1.fill_between(x, y1)
ax1.set_title('remplissage entre y1 et 0')

ax2.fill_between(x, y1, 1)
ax2.set_title('remplissage entre y1 et 1')

ax3.fill_between(x, y1, y2)
ax3.set_title('remplissage entre y1 et y2')
ax3.set_xlabel('x')
fig.tight_layout()
```
