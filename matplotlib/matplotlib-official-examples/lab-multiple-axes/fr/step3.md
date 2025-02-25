# Dessiner le cercle et le point initial

La troisième étape consiste à dessiner le cercle et le point initial sur le sous-graphique de gauche. Nous créons un tableau d'angles pour générer le cercle, puis traçons le sinus et le cosinus de chaque angle. Nous traçons également un seul point à l'origine.

```python
x = np.linspace(0, 2 * np.pi, 50)
axl.plot(np.cos(x), np.sin(x), "k", lw=0.3)
point, = axl.plot(0, 0, "o")
```
