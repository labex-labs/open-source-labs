# Enregistrer le tracé

Nous pouvons enregistrer le tracé sous forme de fichier image à l'aide de la fonction `savefig`.

```python
fig, ax = plt.subplots()
for shape in shapes:
    ax.add_artist(shape)
plt.xlim([-0.5, 1.5])
plt.ylim([-0.5, 1.5])
plt.axis('off')
plt.savefig('shapes.png')
```
