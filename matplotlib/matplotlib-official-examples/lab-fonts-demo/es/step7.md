# Negrita cursiva

La última propiedad de fuente que exploraremos es una combinación de las opciones de estilo y grosor. Esta propiedad le permite establecer el estilo y el grosor de fuente utilizados en su gráfica.

```python
# Muestra negrita cursiva
font = FontProperties(style='italic', weight='bold', size='x-small')
fig.text(0.3, 0.1, 'bold italic', fontproperties=font, **alignment)
font = FontProperties(style='italic', weight='bold', size='medium')
fig.text(0.3, 0.2, 'bold italic', fontproperties=font, **alignment)
font = FontProperties(style='italic', weight='bold', size='x-large')
fig.text(0.3, 0.3, 'bold italic', fontproperties=font, **alignment)
```
