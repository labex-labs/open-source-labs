# Zeichnen eines Kreises mit ungleichem Achsenverhältnis

Wir zeichnen zunächst einen Kreis mit ungleichem Achsenverhältnis, um die Wichtigkeit des Einstellens gleicher Achsenverhältnisse zu demonstrieren.

```python
an = np.linspace(0, 2 * np.pi, 100)
fig, axs = plt.subplots(2, 2)

axs[0, 0].plot(3 * np.cos(an), 3 * np.sin(an))
axs[0, 0].set_title('ungleich, sieht aus wie Ellipse', fontsize=10)
```

Das resultierende Diagramm wird einen Kreis zeigen, der aufgrund des ungleichen Achsenverhältnisses verlängert erscheint.
