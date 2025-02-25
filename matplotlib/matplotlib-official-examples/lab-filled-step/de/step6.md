# Generiere zufällige Daten

Wir werden zufällige Daten mithilfe von `numpy.random.randn` generieren. Wir werden 4 Datensätze mit jeweils 12250 Punkten generieren.

```python
np.random.seed(19680801)
stack_data = np.random.randn(4, 12250)
```
