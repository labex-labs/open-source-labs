# Dessiner la courbe sinusoidale

La quatrième étape consiste à dessiner la courbe sinusoidale sur le sous-graphique de droite. Nous créons un tableau d'angles, puis traçons le sinus de chaque angle. Nous enregistrons également l'objet de tracé `sine`, que nous mettrons à jour plus tard dans l'animation.

```python
sine, = axr.plot(x, np.sin(x))
```
