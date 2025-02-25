# Daten aufniederschlüsseln

Wir werden eine Methode `downsample` definieren, die die Daten aufniederschlüsselt. Die Methode wird die xstart und xend als Eingabeparameter entgegennehmen. Wir werden die Punkte im Anzeigebereich erhalten und die Maske um eins erweitern, um die Punkte direkt außerhalb des Anzeigebereichs zu erfassen, um die Linie nicht abzuschneiden. Wir werden herausfinden, wie viele Punkte weggelassen werden sollen, und die Daten maskieren. Schließlich werden wir die Daten aufniederschlüsseln und die xdata und ydata zurückgeben.

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
