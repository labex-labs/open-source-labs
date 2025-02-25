# Vorbereiten der Beispielsdaten

Wir werden die Funktion `get_sample_data` aus cbook verwenden, um Beispielsdaten zu erhalten. Anschließend werden wir die Bilder vorbereiten, die im Gitter angezeigt werden sollen.

```python
Z = cbook.get_sample_data("axes_grid/bivariate_normal.npy")
extent = (-3, 4, -4, 3)
ZS = [Z[i::3, :] for i in range(3)]
extent = extent[0], extent[1]/3., extent[2], extent[3]
```
