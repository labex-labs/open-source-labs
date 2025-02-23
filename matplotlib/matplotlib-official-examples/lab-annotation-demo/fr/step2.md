# Utilisation de multiples systèmes de coordonnées et de types d'axes

Vous pouvez spécifier le `xypoint` et le `xytext` dans des positions et des systèmes de coordonnées différents, et facultativement activer une ligne de connexion et marquer le point avec un marqueur. Les annotations fonctionnent également sur des axes polaires.

```python
fig, ax = plt.subplots(subplot_kw=dict(projection='polar'), figsize=(3, 3))
r = np.arange(0, 1, 0.001)
theta = 2*2*np.pi*r
line, = ax.plot(theta, r)

ind = 800
thisr, thistheta = r[ind], theta[ind]
ax.plot([thistheta], [thisr], 'o')
ax.annotate('une annotation polaire',
            xy=(thistheta, thisr),  # theta, rayon
            xytext=(0.05, 0.05),    # fraction, fraction
            textcoords='fraction de figure',
            arrowprops=dict(facecolor='black', shrink=0.05),
            horizontalalignment='left',
            verticalalignment='bottom')
```
