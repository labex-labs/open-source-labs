# Mise à jour des données

Nous allons définir une méthode `update` qui mettra à jour les données. La méthode prendra `ax` (axe) comme paramètre d'entrée. Nous mettrons à jour la ligne en obtenant la limite d'affichage et en vérifiant si la largeur de la limite d'affichage est différente de `delta`. Si la largeur de la limite d'affichage est différente de `delta`, nous mettrons à jour `delta` et obtiendrons `xstart` et `xend`. Nous définirons ensuite les données sur les données rééchantillonnées et dessinerons l'état inactif.

```python
def update(self, ax):
    # Update the line
    lims = ax.viewLim
    if abs(lims.width - self.delta) > 1e-8:
        self.delta = lims.width
        xstart, xend = lims.intervalx
        self.line.set_data(*self.downsample(xstart, xend))
        ax.figure.canvas.draw_idle()
```
