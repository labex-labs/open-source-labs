# Schwellwerte definieren

```python
x_values = np.arange(0.4, 1.05, 0.05)
x_values = np.append(x_values, 0.99999)
```

Wir definieren einen Array von Schwellwerten, der von 0,4 bis 1 reicht, mit Schritten von 0,05. Anschließend fügen wir einen sehr hohen Schwellwert von 0,99999 hinzu, um sicherzustellen, dass wir einen Schwellwert enthalten, der keine selbst zugewiesenen Proben hervorruft.
