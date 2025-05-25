# Adicionar Linhas Verticais

Nesta etapa, adicionaremos linhas verticais ao gráfico. Usaremos a função `vlines` do Matplotlib para desenhar as linhas verticais. Também usaremos o parâmetro `transform` para definir as coordenadas y para serem escaladas de 0 a 1. Desenhararemos duas linhas verticais em x=1 e x=2.

```python
# Add vertical lines
vax.plot(t, s + nse, '^')
vax.vlines(t, [0], s)
vax.vlines([1, 2], 0, 1, transform=vax.get_xaxis_transform(), colors='r')
vax.set_xlabel('time (s)')
vax.set_title('Vertical lines demo')
```
