# Den Null-Locator definieren

Der Null-Locator ist ein Locator, der keine Striche auf der Achse platziert. Wir können den Null-Locator mit `ticker.NullLocator()` definieren.

```python
setup(axs[0], title="NullLocator()")
axs[0].xaxis.set_major_locator(ticker.NullLocator())
axs[0].xaxis.set_minor_locator(ticker.NullLocator())
```
