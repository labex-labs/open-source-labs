# Normalisieren der Daten

Um eine geschattete und leistungsnormalisierte Darstellung der Mandelbrot-Menge zu erstellen, müssen wir unsere Daten normalisieren. Wir werden dies mit der folgenden Formel tun:

`M = N + 1 - np.log2(np.log(abs(Z))) + log_horizon`

```python
with np.errstate(invalid='ignore'):
    M = np.nan_to_num(N + 1 - np.log2(np.log(abs(Z))) + log_horizon)
```
