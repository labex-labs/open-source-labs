# Aplicando TickedStroke às linhas

Nesta etapa, aplicaremos TickedStroke às linhas.

```python
fig, ax = plt.subplots(figsize=(6, 6))
ax.plot([0, 1], [0, 1], label="Line",
        path_effects=[patheffects.withTickedStroke(spacing=7, angle=135)])

nx = 101
x = np.linspace(0.0, 1.0, nx)
y = 0.3*np.sin(x*8) + 0.4
ax.plot(x, y, label="Curve", path_effects=[patheffects.withTickedStroke()])

ax.legend()

plt.show()
```

Este código criará uma linha e uma curva com o efeito de caminho TickedStroke.
