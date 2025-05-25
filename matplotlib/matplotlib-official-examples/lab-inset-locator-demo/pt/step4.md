# Controlar a Posição e o Tamanho do _Inset_

Podemos usar os parâmetros `bbox_to_anchor` e `bbox_transform` para controlar a posição e o tamanho do _inset_. Estes parâmetros permitem um controle preciso sobre a posição e o tamanho do _inset_ ou até mesmo posicionar o _inset_ em posições completamente arbitrárias.

```python
# Usamos a transformação dos eixos como bbox_transform. Portanto, a caixa delimitadora
# precisa ser especificada em coordenadas dos eixos ((0, 0) é o canto inferior esquerdo
# dos eixos, (1, 1) é o canto superior direito).
# A caixa delimitadora (.2, .4, .6, .5) começa em (.2, .4) e se estende até (.8, .9)
# nessas coordenadas.
# Dentro desta caixa delimitadora, um inset com metade da largura da caixa delimitadora e
# três quartos da altura da caixa delimitadora é criado. O canto inferior esquerdo
# do inset é alinhado ao canto inferior esquerdo da caixa delimitadora (loc=3).
# O inset é então deslocado pelo padrão de 0.5 em unidades do tamanho da fonte.
axins = inset_axes(ax, width="50%", height="75%",
                   bbox_to_anchor=(.2, .4, .6, .5),
                   bbox_transform=ax.transAxes, loc=3)
```
