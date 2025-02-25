# Rééchantillonnage des données

Nous allons définir une méthode `downsample` qui réduira l'échantillonnage des données. La méthode prendra `xstart` et `xend` comme paramètres d'entrée. Nous obtiendrons les points dans la plage d'affichage et dilaterons le masque de un pour capturer les points juste en dehors de la plage d'affichage afin de ne pas tronquer la ligne. Nous déterminerons combien de points doivent être éliminés et nous masquerons les données. Enfin, nous réduirons l'échantillonnage des données et renverrons les données x et y.

```python
def downsample(self, xstart, xend):
    # get the points in the view range
    mask = (self.origXData > xstart) & (self.origXData < xend)
    # dilate the mask by one to catch the points just outside
    # of the view range to not truncate the line
    mask = np.convolve([1, 1, 1], mask, mode='same').astype(bool)
    # sort out how many points to drop
    ratio = max(np.sum(mask) // self.max_points, 1)

    # mask data
    xdata = self.origXData[mask]
    ydata = self.origYData[mask]

    # downsample data
    xdata = xdata[::ratio]
    ydata = ydata[::ratio]

    print(f"using {len(ydata)} of {np.sum(mask)} visible points")

    return xdata, ydata
```
