# Criar um _Inset_ com uma Caixa Delimitadora de 2-Tuplas

Podemos criar um _inset_ com uma caixa delimitadora de 2-tuplas especificando a largura e a altura em polegadas e usando o parâmetro `bbox_to_anchor` para especificar o canto inferior esquerdo do _inset_.

```python
# Criar um inset com uma caixa delimitadora de 2-tuplas. Note que isso cria uma
# bbox sem extensão. Portanto, isso só faz sentido ao especificar
# largura e altura em unidades absolutas (polegadas).
axins2 = inset_axes(ax, width=0.5, height=0.4,
                    bbox_to_anchor=(0.33, 0.25),
                    bbox_transform=ax.transAxes, loc=3, borderpad=0)
```
