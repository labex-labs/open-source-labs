# Ein Kernel-Dichteschätzer anpassen

Jetzt werden wir eine Instanz des `KernelDensity`-Schätzers erstellen und ihn an unsere Daten anpassen. Wir können den Typ des Kerns und die Bandbreite für den Schätzer auswählen. Beispielsweise können wir einen Gaußschen Kern verwenden und die Bandbreite auf 0,2 setzen.

```python
kde = KernelDensity(kernel='gaussian', bandwidth=0.2).fit(X)
```
