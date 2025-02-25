# Créez un tracé

Nous allons maintenant créer un tracé pour y ajouter des annotations. Le code suivant créera un tracé avec deux points de données.

```python
fig, ax = plt.subplots()
x = [1, 2]
y = [3, 4]
ax.plot(x, y, "o")
```
