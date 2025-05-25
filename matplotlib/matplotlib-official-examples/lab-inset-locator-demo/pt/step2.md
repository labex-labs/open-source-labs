# Criar Eixos de _Inset_

Em seguida, criaremos eixos de _inset_ (janelas internas) em cada um dos _subplots_. Usaremos o método `inset_axes()` para criar os eixos de _inset_. Criaremos quatro _insets_ com diferentes tamanhos e localizações.

```python
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

# Criar inset com largura de 1.3 polegadas e altura de 0.9 polegadas
# na localização padrão superior direita
axins = inset_axes(ax, width=1.3, height=0.9)

# Criar inset com largura de 30% e altura de 40% da caixa delimitadora dos eixos pai
# no canto inferior esquerdo (loc=3)
axins2 = inset_axes(ax, width="30%", height="40%", loc=3)

# Criar inset com especificações mistas no segundo subplot;
# a largura é 30% da caixa delimitadora dos eixos pai e
# a altura é 1 polegada no canto superior esquerdo (loc=2)
axins3 = inset_axes(ax2, width="30%", height=1., loc=2)

# Criar um inset no canto inferior direito (loc=4) com borderpad=1, ou seja,
# preenchimento de 10 pontos (pois 10pt é o tamanho de fonte padrão) para os eixos pai
axins4 = inset_axes(ax2, width="20%", height="20%", loc=4, borderpad=1)
```
