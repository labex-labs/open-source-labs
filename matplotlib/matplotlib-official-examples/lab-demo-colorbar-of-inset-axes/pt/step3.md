# Criar um Eixo Inserido (Inset Axis)

Crie um eixo inserido usando a função `zoomed_inset_axes`. Defina o nível de zoom e a localização do eixo inserido dentro do gráfico principal.

```python
axins = zoomed_inset_axes(ax, zoom=2, loc='upper left')
axins.set(xticks=[], yticks=[])
```
