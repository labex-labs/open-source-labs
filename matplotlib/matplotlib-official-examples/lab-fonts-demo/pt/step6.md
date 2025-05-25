# Opções de Tamanho

A quinta propriedade de fonte que exploraremos é a opção de tamanho (size). Essa propriedade permite que você defina o tamanho da fonte usado em seu gráfico.

```python
# Show size options
sizes = [
    'xx-small', 'x-small', 'small', 'medium', 'large', 'x-large', 'xx-large']
fig.text(0.9, 0.9, 'size', fontproperties=heading_font, **alignment)
for k, size in enumerate(sizes):
    font = FontProperties()
    font.set_size(size)
    fig.text(0.9, yp[k], size, fontproperties=font, **alignment)
```
