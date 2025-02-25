# Daten erstellen

Als nächstes erstellen wir die Daten, die wir in unserem Diagramm verwenden werden. In diesem Beispiel verwenden wir NumPy, um die Daten zu generieren.

```python
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X ** 2 + Y ** 2))
```
