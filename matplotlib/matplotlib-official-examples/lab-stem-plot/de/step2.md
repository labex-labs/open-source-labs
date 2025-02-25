# Daten generieren

Als nächstes müssen wir einige Daten generieren, die wir in unserem Stammdiagramm verwenden möchten. Wir werden zwei Arrays mit der Numpy-Bibliothek erstellen.

```python
x = np.linspace(0.1, 2 * np.pi, 41)
y = np.exp(np.sin(x))
```
