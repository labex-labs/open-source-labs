# Plotar a triangulação, as iso-curvas de potencial e o campo vetorial

```python
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.use_sticky_edges = False
ax.margins(0.07)

ax.triplot(triang, color='0.8')

levels = np.arange(0., 1., 0.01)
ax.tricontour(tri_refi, z_test_refi, levels=levels, cmap='hot',
              linewidths=[2.0, 1.0, 1.0, 1.0])

ax.quiver(triang.x, triang.y, Ex/E_norm, Ey/E_norm,
          units='xy', scale=10., zorder=3, color='blue',
          width=0.007, headwidth=3., headlength=4.)

ax.set_title('Gradient Plot: Electrical Dipole')
plt.show()
```

Explicação:

- `fig` e `ax` são, respectivamente, os objetos de figura e eixos.
- `ax.set_aspect` define a proporção do aspecto dos eixos.
- `ax.use_sticky_edges` e `ax.margins` definem as margens dos eixos.
- `ax.triplot` plota a triangulação.
- `ax.tricontour` plota as iso-curvas de potencial.
- `ax.quiver` plota o campo vetorial.
- `ax.set_title` define o título do gráfico.
