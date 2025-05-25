# Criar o Gráfico e a Imagem

Em seguida, criaremos um gráfico e uma imagem para mostrar como adicionar uma barra de cores usando eixos inseridos (inset axes).

```python
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=[6, 3])

im1 = ax1.imshow([[1, 2], [2, 3]])
im2 = ax2.imshow([[1, 2], [2, 3]])
```
