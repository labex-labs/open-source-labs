# Alternar a exibição de diferentes elementos

Podemos alternar a exibição de diferentes elementos do boxplot usando vários parâmetros na função `bxp()`. Neste exemplo, demonstramos como mostrar ou ocultar a média, a caixa (box), as extremidades (caps), os entalhes (notches) e os valores discrepantes (fliers).

```python
# Toggle the display of different elements
plt.bxp(stats, showmeans=True, showbox=False, showcaps=False, shownotches=True, showfliers=False)
plt.show()
```
