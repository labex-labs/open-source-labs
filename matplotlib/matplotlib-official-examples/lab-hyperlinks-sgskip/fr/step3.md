# Créer une image avec un lien hypertexte

Dans cette étape, nous allons créer une image et lui ajouter un lien hypertexte. Voici le code pour créer l'image :

```python
fig = plt.figure()
delta = 0.025
x = y = np.arange(-3.0, 3.0, delta)
X, Y = np.meshgrid(x, y)
Z1 = np.exp(-X**2 - Y**2)
Z2 = np.exp(-(X - 1)**2 - (Y - 1)**2)
Z = (Z1 - Z2) * 2

im = plt.imshow(Z, interpolation='bilinear', cmap=cm.gray,
                origin='lower', extent=[-3, 3, -3, 3])
```

Pour ajouter un lien hypertexte à l'image, nous devons utiliser la méthode `set_url()` de l'objet image. Cette méthode prend une URL en argument. Voici le code mis à jour :

```python
im.set_url('https://www.google.com/')
```

L'image aura un lien hypertexte vers `https://www.google.com/`. Enfin, nous pouvons enregistrer le graphique sous forme de fichier SVG en utilisant `fig.savefig()` :

```python
fig.savefig('image.svg')
```
