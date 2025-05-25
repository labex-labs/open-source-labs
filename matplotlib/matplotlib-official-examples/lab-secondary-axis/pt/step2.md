# Plotar os dados

Criaremos uma onda senoidal simples para demonstrar o uso de um eixo secundário. Plotaremos a onda senoidal usando graus como o eixo x.

```python
fig, ax = plt.subplots(layout='constrained')
x = np.arange(0, 360, 1)
y = np.sin(2 * x * np.pi / 180)
ax.plot(x, y)
ax.set_xlabel('angle [degrees]')
ax.set_ylabel('signal')
ax.set_title('Sine wave')
```
