# Créez les sous-graphiques

Nous allons créer une figure avec deux sous-graphiques à l'aide de `.pyplot.subplot`.

```python
plt.figure()

plt.subplot(211)
plt.plot(t1, f(t1), color='tab:blue', marker='o')
plt.plot(t2, f(t2), color='black')

plt.subplot(212)
plt.plot(t2, np.cos(2*np.pi*t2), color='tab:orange', linestyle='--')

plt.show()
```

La fonction `subplot()` prend trois arguments : le nombre de lignes, le nombre de colonnes et l'index du tracé actuel. L'index commence à 1 dans le coin supérieur gauche et augmente ligne par ligne. Dans cet exemple, nous créons une figure avec deux sous-graphiques : l'un en haut et l'autre en bas.

Dans le premier sous-graphique, nous traçons `t1` en fonction de `f(t1)` et `t2` en fonction de `f(t2)`. Nous définissons la couleur du premier tracé en bleu et ajoutons des marqueurs circulaires à chaque point de données. Nous définissons la couleur du second tracé en noir.

Dans le second sous-graphique, nous traçons `t2` en fonction de la fonction cosinus de `2*np.pi*t2`. Nous définissons la couleur du tracé en orange et le style de ligne en tirets.
