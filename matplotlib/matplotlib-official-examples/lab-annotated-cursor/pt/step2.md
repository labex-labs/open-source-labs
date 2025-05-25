# Criar um gráfico

Criamos um gráfico simples de uma parábola usando a função `linspace` do NumPy para gerar 1000 valores entre -5 e 5 para x, e então calculamos y como o quadrado de x.

```python
fig, ax = plt.subplots(figsize=(8, 6))
ax.set_title("Cursor Tracking x Position")

x = np.linspace(-5, 5, 1000)
y = x**2

line, = ax.plot(x, y)
ax.set_xlim(-5, 5)
ax.set_ylim(0, 25)
```
