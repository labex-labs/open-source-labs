# Apporter des modifications à la figure 1

Maintenant, nous allons revenir à la première figure et apporter quelques modifications. Nous allons tracer la deuxième onde sinusoïdale dans le sous-graphique supérieur en utilisant des marqueurs carrés, et supprimer les étiquettes d'échelonnement de l'axe x du sous-graphique supérieur.

```python
plt.figure(1)

# Sous-graphique supérieur
plt.subplot(211)
plt.plot(t, s2,'s')
ax = plt.gca()
ax.set_xticklabels([])
```
