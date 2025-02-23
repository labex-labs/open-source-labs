# Crear un gráfico

Creamos un gráfico simple de una parábola utilizando la función `linspace` de NumPy para generar 1000 valores entre -5 y 5 para x, y luego calcular y como el cuadrado de x.

```python
fig, ax = plt.subplots(figsize=(8, 6))
ax.set_title("Cursor Tracking x Position")

x = np.linspace(-5, 5, 1000)
y = x**2

line, = ax.plot(x, y)
ax.set_xlim(-5, 5)
ax.set_ylim(0, 25)
```
