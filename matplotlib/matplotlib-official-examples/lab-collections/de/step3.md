# Verschiebungen erstellen

```python
# Fixing random state for reproducibility
rs = np.random.RandomState(19680801)

# Make some offsets
xyo = rs.randn(npts, 2)
```

Als dritten Schritt erstellen wir Verschiebungen mit Numpy. Wir werden die Zufallsfunktion verwenden, um die Verschiebungen zu erstellen.
