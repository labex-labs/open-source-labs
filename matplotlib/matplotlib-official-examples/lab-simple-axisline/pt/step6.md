# Criar Eixo Y2

Finalmente, criaremos um novo eixo y2 no lado direito do gráfico com um deslocamento (offset) de (20, 0) e o rotularemos.

```python
ax.axis["right2"] = ax.new_fixed_axis(loc="right", offset=(20, 0))
ax.axis["right2"].label.set_text("Label Y2")
```
