# Zufällige Daten generieren

Wir werden einige zufällige Daten generieren, um sie für das Streudiagramm und die Histogramme zu verwenden.

```python
# Fixing random state for reproducibility
np.random.seed(19680801)

# Generate random data
x = np.random.randn(1000)
y = np.random.randn(1000)
```
