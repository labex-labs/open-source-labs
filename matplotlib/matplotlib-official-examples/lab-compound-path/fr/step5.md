# Création du tracé

Nous allons créer le tracé et ajouter le `PathPatch` au tracé. Nous allons définir le titre du tracé sur `'Un chemin composé'`.

```python
fig, ax = plt.subplots()
ax.add_patch(pathpatch)
ax.set_title('A Compound Path')

ax.autoscale_view()

plt.show()
```
