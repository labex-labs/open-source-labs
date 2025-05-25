# Criar Espaço para o Rótulo do Eixo Y e Ajustar os Eixos

Nesta etapa, usamos o método `make_axes_area_auto_adjustable` para criar espaço para o rótulo do eixo y em ambos os eixos. Também usamos o parâmetro `use_axes` para especificar os eixos a serem ajustados e o parâmetro `pad` para ajustar o espaçamento entre os eixos.

```python
make_axes_area_auto_adjustable(ax1, pad=0.1, use_axes=[ax1, ax2])
make_axes_area_auto_adjustable(ax2, pad=0.1, use_axes=[ax1, ax2])
```
