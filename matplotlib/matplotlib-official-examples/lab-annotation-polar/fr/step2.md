# Créer un graphique polaire

Ensuite, nous créons un graphique polaire en définissant la figure et en spécifiant qu'elle a une projection polaire. Nous définissons également les valeurs de rayon et de theta à utiliser pour le tracé.

```python
fig = plt.figure()
ax = fig.add_subplot(projection='polar')
r = np.arange(0, 1, 0.001)
theta = 2 * 2*np.pi * r
line, = ax.plot(theta, r, color='#ee8d18', lw=3)
```
