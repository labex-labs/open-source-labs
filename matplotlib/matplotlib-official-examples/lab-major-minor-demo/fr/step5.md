# Sélection automatique des étiquettes graduées pour les étiquettes graduées principales et mineures

```python
# Créez des données
t = np.arange(0.0, 100.0, 0.01)
s = np.sin(2 * np.pi * t) * np.exp(-t * 0.01)

# Tracez les données
fig, ax = plt.subplots()
ax.plot(t, s)

# Définissez le localisateur mineur
ax.xaxis.set_minor_locator(AutoMinorLocator())

# Définissez les paramètres des étiquettes graduées
ax.tick_params(which='both', width=2)
ax.tick_params(which='major', length=7)
ax.tick_params(which='minor', length=4, color='r')

# Affichez le graphique
plt.show()
```

Dans cette étape, nous créons de nouvelles données et les traçons. Ensuite, nous définissons le localisateur mineur pour sélectionner automatiquement le nombre d'étiquettes graduées mineures. Après cela, nous définissons les paramètres des étiquettes graduées, c'est-à-dire la largeur et la longueur des étiquettes graduées et leur couleur, pour les étiquettes graduées principales et mineures. Enfin, nous affichons le graphique.
