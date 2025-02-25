# Création du tracé

Nous allons créer un tracé à l'aide de Matplotlib. Nous allons créer une instance `d` de la classe `DataDisplayDownsampler` en utilisant `xdata` et `ydata`. Nous allons créer une figure et un axe à l'aide de la fonction `subplots`. Nous allons connecter la ligne et définir l'auto-échelle sur `False`. Nous allons connecter pour changer les limites d'affichage, définir la limite x et afficher le tracé.

```python
d = DataDisplayDownsampler(xdata, ydata)
fig, ax = plt.subplots()
d.line, = ax.plot(xdata, ydata, 'o-')
ax.set_autoscale_on(False)
ax.callbacks.connect('xlim_changed', d.update)
ax.set_xlim(16, 365)
plt.show()
```
