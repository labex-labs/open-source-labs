# Den Fixed-Locator definieren

Der Fixed-Locator ist ein Locator, der Striche an festen Positionen platziert. Wir können den Fixed-Locator mit `ticker.FixedLocator()` definieren.

```python
setup(axs[2], title="FixedLocator([0, 1, 5])")
axs[2].xaxis.set_major_locator(ticker.FixedLocator([0, 1, 5]))
axs[2].xaxis.set_minor_locator(ticker.FixedLocator(np.linspace(0.2, 0.8, 4)))
```
