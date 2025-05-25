# Ajustar Eixos Parasitas

Precisamos ajustar a posição dos eixos parasitas. A função `new_fixed_axis()` é usada para criar um novo eixo y no lado direito do gráfico. A função `toggle()` é usada para ativar todos os ticks e rótulos do eixo y direito.

```python
par2.axis["right"] = par2.new_fixed_axis(loc="right", offset=(60, 0))

par1.axis["right"].toggle(all=True)
par2.axis["right"].toggle(all=True)
```
