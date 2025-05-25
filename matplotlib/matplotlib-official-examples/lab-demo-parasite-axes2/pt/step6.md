# Adicionar Legenda e Cor

Adicionaremos uma legenda ao gráfico e coloriremos os rótulos de cada eixo para corresponder à cor do conjunto de dados correspondente, usando as funções `legend()` e `label.set_color()`.

```python
host.legend()

host.axis["left"].label.set_color(p1.get_color())
par1.axis["right"].label.set_color(p2.get_color())
par2.axis["right"].label.set_color(p3.get_color())
```
