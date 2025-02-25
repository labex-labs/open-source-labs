# Definieren der Werte für x, y und z

Wir werden die Werte für x, y und z mit NumPy generieren. Zunächst werden wir den Wertebereich für theta und z definieren. Anschließend werden wir diese Werte verwenden, um die Werte für r, x und y zu generieren.

```python
theta = np.linspace(-4 * np.pi, 4 * np.pi, 100)
z = np.linspace(-2, 2, 100)
r = z**2 + 1
x = r * np.sin(theta)
y = r * np.cos(theta)
```
