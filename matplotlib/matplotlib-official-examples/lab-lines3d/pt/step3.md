# Definir os valores para x, y e z

Geraremos os valores para x, y e z usando NumPy. Primeiro, definiremos a faixa de valores para theta e z. Em seguida, usaremos esses valores para gerar os valores para r, x e y.

```python
theta = np.linspace(-4 * np.pi, 4 * np.pi, 100)
z = np.linspace(-2, 2, 100)
r = z**2 + 1
x = r * np.sin(theta)
y = r * np.cos(theta)
```
