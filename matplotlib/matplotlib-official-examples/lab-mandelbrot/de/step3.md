# Erzeugen der Mandelbrot-Menge

Jetzt werden wir die Mandelbrot-Menge erzeugen, indem wir die `mandelbrot_set`-Funktion mit unseren gewünschten Parametern aufrufen. Dies gibt uns zwei Arrays:

- `Z`: die Endwerte der komplexen Zahlen, über die wir iteriert haben
- `N`: die Anzahl der Iterationen, die für jeden Punkt durchgeführt wurden, bevor er als Teil der Menge bestimmt wurde

```python
xmin, xmax, xn = -2.25, +0.75, 3000 // 2
ymin, ymax, yn = -1.25, +1.25, 2500 // 2
maxiter = 200
horizon = 2.0 ** 40
log_horizon = np.log2(np.log(horizon))
Z, N = mandelbrot_set(xmin, xmax, ymin, ymax, xn, yn, maxiter, horizon)
```
