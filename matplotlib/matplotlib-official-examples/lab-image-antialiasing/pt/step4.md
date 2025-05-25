# Superamostrar Imagem com Interpolação 'nearest'

Agora, faremos a superamostragem da imagem de 500 pixels de dados para 530 pixels renderizados usando a interpolação 'nearest'. Isso demonstrará como os padrões Moiré ainda podem ocorrer mesmo quando a imagem é superamostrada se o fator de superamostragem não for um inteiro.

```python
fig, ax = plt.subplots(figsize=(6.8, 6.8))
ax.imshow(a, interpolation='nearest', cmap='gray')
ax.set_title("upsampled by factor a 1.048, interpolation='nearest'")
plt.show()
```
