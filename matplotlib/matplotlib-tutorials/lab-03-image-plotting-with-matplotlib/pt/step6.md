# Esquemas de Interpolação de Array

Ao redimensionar uma imagem, é necessário interpolar os valores dos pixels para preencher o espaço ausente. Diferentes esquemas de interpolação podem ser usados para determinar o valor de um pixel com base em seus pixels circundantes. Matplotlib fornece diferentes opções de interpolação, como "nearest" (mais próximo), "bilinear" (bilinear) e "bicubic" (bicúbica).

```python
plt.imshow(img, interpolation="bilinear")
```
