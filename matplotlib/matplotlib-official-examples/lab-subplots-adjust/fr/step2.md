# Création de graphiques

Ensuite, créons deux graphiques à l'aide de `imshow` et de tableaux aléatoires générés par `numpy.random`. Nous ajouterons également une barre de couleur aux graphiques. Exécutez le code suivant :

```python
# Fixing random state for reproducibility
np.random.seed(19680801)

plt.subplot(211)
plt.imshow(np.random.random((100, 100)))
plt.subplot(212)
plt.imshow(np.random.random((100, 100)))

cax = plt.axes([0.85, 0.1, 0.075, 0.8])
plt.colorbar(cax=cax)

plt.show()
```
