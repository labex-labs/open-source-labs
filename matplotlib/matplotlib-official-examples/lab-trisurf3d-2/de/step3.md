# Definieren der Fläche

Als nächstes definieren wir die Fläche. In diesem Beispiel verwenden wir eine Möbiustransformation, um ein `u`-`v`-Paar zu nehmen und ein `x`-`y`-`z`-Tripel zurückzugeben.

```python
x = (1 + 0.5 * v * np.cos(u / 2.0)) * np.cos(u)
y = (1 + 0.5 * v * np.cos(u / 2.0)) * np.sin(u)
z = 0.5 * v * np.sin(u / 2.0)
```
