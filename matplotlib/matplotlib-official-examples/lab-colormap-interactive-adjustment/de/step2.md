# Generiere Daten

Als nächstes wirst du einige Beispiel-Daten generieren. In diesem Lab werden wir eine zweidimensionale Sinuswelle generieren.

```python
t = np.linspace(0, 2 * np.pi, 1024)
data2d = np.sin(t)[:, np.newaxis] * np.cos(t)[np.newaxis, :]
```
