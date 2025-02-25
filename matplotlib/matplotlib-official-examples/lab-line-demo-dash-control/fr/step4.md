# Créez le tracé

Maintenant, nous pouvons créer le tracé en utilisant la fonction `plt.subplots()`. Nous allons également créer trois lignes en utilisant la fonction `ax.plot()`.

```python
fig, ax = plt.subplots()

# Utilisation de set_dashes() et set_capstyle() pour modifier le trait discontinu d'une ligne existante.
line1, = ax.plot(x, y, label='Using set_dashes() and set_dash_capstyle()')
line1.set_dashes([2, 2, 10, 2])  # Ligne de 2pt, interruption de 2pt, ligne de 10pt, interruption de 2pt.
line1.set_dash_capstyle('round')

# Utilisation de plot(..., dashes=...) pour définir le trait discontinu lors de la création d'une ligne.
line2, = ax.plot(x, y - 0.2, dashes=[6, 2], label='Using the dashes parameter')

# Utilisation de plot(..., dashes=..., gapcolor=...) pour définir le trait discontinu et
# la couleur alternative lors de la création d'une ligne.
line3, = ax.plot(x, y - 0.4, dashes=[4, 4], gapcolor='tab:pink',
                 label='Using the dashes and gapcolor parameters')

ax.legend(handlelength=4)
plt.show()
```
