# Adicionar Linhas Horizontais

Nesta etapa, adicionaremos linhas horizontais ao gráfico. Usaremos a função `hlines` do Matplotlib para desenhar as linhas horizontais. Desenhararemos linhas horizontais em y=0.5, y=2.5 e y=4.5.

```python
# Add horizontal lines
hax.plot(s + nse, t, '^')
hax.hlines(t, [0], s, lw=2)
hax.set_xlabel('time (s)')
hax.set_title('Horizontal lines demo')
```
