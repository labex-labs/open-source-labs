# Aplicando Esquemas de Pseudocor

Esquemas de pseudocor podem ser usados para aprimorar o contraste e visualizar dados com mais facilidade. Se a imagem for em tons de cinza (grayscale), podemos aplicar esquemas de pseudocor especificando diferentes mapas de cores (colormaps). Podemos fazer isso usando o parâmetro `cmap` na função `imshow`.

```python
lum_img = img[:, :, 0]
plt.imshow(lum_img, cmap="hot")
```
