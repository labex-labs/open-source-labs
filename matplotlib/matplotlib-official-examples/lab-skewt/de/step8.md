# SkewT-logP-Diagramm erstellen

Wir werden nun das SkewT-logP-Diagramm mit der zuvor registrierten SkewXAxes-Projection erstellen. Zunächst werden wir ein Figure-Objekt erstellen und ein Subplot mit der SkewXAxes-Projection hinzufügen. Anschließend werden wir die Temperatur- und Taupunkt-Daten auf dem Diagramm mit der semilogy-Funktion plotten. Schließlich werden wir die Grenzen und Markierungen für die X- und Y-Achse festlegen und das Diagramm anzeigen.

```python
fig = plt.figure(figsize=(6.5875, 6.2125))
ax = fig.add_subplot(projection='skewx')

ax.semilogy(T, p, color='C3')
ax.semilogy(Td, p, color='C2')

ax.axvline(0, color='C0')

ax.yaxis.set_major_formatter(ScalarFormatter())
ax.yaxis.set_minor_formatter(NullFormatter())
ax.set_yticks(np.linspace(100, 1000, 10))
ax.set_ylim(1050, 100)

ax.xaxis.set_major_locator(MultipleLocator(10))
ax.set_xlim(-50, 50)

plt.grid(True)
plt.show()
```
