# Definir Zoom e Ângulo de Visualização

Defina o zoom e o ângulo de visualização usando os métodos `view_init` e `set_box_aspect`. Definiremos o ângulo de visualização para 40 graus na direção X e -30 graus na direção Y, e o zoom para 0.9.

```python
# Set zoom and angle view
ax.view_init(40, -30, 0)
ax.set_box_aspect(None, zoom=0.9)
```
