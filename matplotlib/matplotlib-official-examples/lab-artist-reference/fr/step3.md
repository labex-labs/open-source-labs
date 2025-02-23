# Dessiner les formes

Nous allons maintenant tracer les formes à l'aide de Matplotlib en parcourant la liste `shapes` et en les ajoutant au tracé.

```python
fig, ax = plt.subplots()
for shape in shapes:
    ax.add_artist(shape)
plt.xlim([-0.5, 1.5])
plt.ylim([-0.5, 1.5])
plt.axis('off')
plt.show()
```
