# Simple démonstration de Pcolor

La première étape est de créer une simple démonstration de Pcolor. Cela vous montrera comment créer un graphique Pcolor de base.

```python
Z = np.random.rand(6, 10)

fig, (ax0, ax1) = plt.subplots(2, 1)

c = ax0.pcolor(Z)
ax0.set_title('par défaut : pas de bords')

c = ax1.pcolor(Z, edgecolors='k', linewidths=4)
ax1.set_title('bords épais')

fig.tight_layout()
plt.show()
```
