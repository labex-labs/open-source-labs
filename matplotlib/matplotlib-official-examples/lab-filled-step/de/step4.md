# Einrichten der Histogrammfunktion mit fester Binung

Wir werden eine Histogrammfunktion mit fester Binung mithilfe von `numpy.histogram` einrichten. Wir werden 20 Bins erstellen, die von -3 bis 3 reichen.

```python
edges = np.linspace(-3, 3, 20, endpoint=True)
hist_func = partial(np.histogram, bins=edges)
```
