# Configurar o Estilo do Eixo

Agora configuraremos o estilo do eixo adicionando setas nas extremidades de cada eixo e adicionando os eixos X e Y a partir da origem.

```python
for direction in ["xzero", "yzero"]:
    # adds arrows at the ends of each axis
    ax.axis[direction].set_axisline_style("-|>")
    # adds X and Y-axis from the origin
    ax.axis[direction].set_visible(True)

# hides borders
for direction in ["left", "right", "bottom", "top"]:
    ax.axis[direction].set_visible(False)
```
