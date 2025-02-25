# Créer un graphique en nuage de points

Nous allons créer un graphique en nuage de points avec des couleurs et des tailles de marqueurs variables en utilisant les valeurs calculées.

```python
fig, ax = plt.subplots()
ax.scatter(delta1[:-1], delta1[1:], c=close, s=volume, alpha=0.5)

ax.set_xlabel(r'$\Delta_i$', fontsize=15)
ax.set_ylabel(r'$\Delta_{i+1}$', fontsize=15)
ax.set_title('Volume et changement en pourcentage')

ax.grid(True)
fig.tight_layout()

plt.show()
```
