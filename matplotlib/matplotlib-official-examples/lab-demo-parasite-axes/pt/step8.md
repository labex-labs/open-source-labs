# Adicionar legenda e cores dos eixos

Adicionamos uma legenda aos eixos host usando o método `host.legend()`. Também definimos a cor do rótulo do eixo y esquerdo dos eixos host, o rótulo do eixo y direito do primeiro eixo parasita e o rótulo do eixo y direito do segundo eixo parasita para corresponder às suas respectivas linhas usando os métodos `host.axis["left"].label.set_color(p1.get_color())`, `par1.axis["right"].label.set_color(p2.get_color())` e `par2.axis["right2"].label.set_color(p3.get_color())`.

```python
host.legend()

host.axis["left"].label.set_color(p1.get_color())
par1.axis["right"].label.set_color(p2.get_color())
par2.axis["right2"].label.set_color(p3.get_color())
```
