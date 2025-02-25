# Zeichnen eines weiteren Beispiels

Wir werden jetzt ein weiteres Beispiel zeichnen, bei dem die Umrechnung von Wellenzahl in Wellenlänge in einem doppelt-logarithmischen Maßstab erfolgt. Für dieses Beispiel werden wir ein zufälliges Spektrum verwenden.

```python
fig, ax = plt.subplots(layout='constrained')
x = np.arange(0.02, 1, 0.02)
np.random.seed(19680801)
y = np.random.randn(len(x)) ** 2
ax.loglog(x, y)
ax.set_xlabel('f [Hz]')
ax.set_ylabel('PSD')
ax.set_title('Random spectrum')
```
