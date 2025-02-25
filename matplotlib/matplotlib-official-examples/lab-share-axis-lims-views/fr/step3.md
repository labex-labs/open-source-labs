# Créez la première figure

Maintenant, créons la première figure en utilisant `subplot`. `subplot` prend trois arguments : le nombre de lignes, le nombre de colonnes et le numéro de la figure. Dans cet exemple, nous allons créer une figure avec 2 lignes et 1 colonne (`211`), ce qui signifie que la première figure sera dans la première ligne.

```python
ax1 = plt.subplot(211)
ax1.plot(t, np.sin(2*np.pi*t))
```
