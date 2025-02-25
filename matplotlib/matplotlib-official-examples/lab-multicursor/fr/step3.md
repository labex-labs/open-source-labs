# Création de graphiques

Maintenant, nous allons créer trois sous-graphiques en utilisant la fonction `plt.subplots`. Deux graphiques seront créés dans une même figure, tandis que le troisième graphique sera créé dans une figure séparée.

```python
fig, (ax1, ax2) = plt.subplots(2, sharex=True)
ax1.plot(t, s1)
ax2.plot(t, s2)
fig, ax3 = plt.subplots()
ax3.plot(t, s3)
```
