# Superamostrar Imagem com Interpolação 'antialiased'

Finalmente, faremos a superamostragem da imagem de 500 pixels de dados para 530 pixels renderizados usando a interpolação 'antialiased'. Isso demonstrará como o uso de algoritmos de antialiasing melhores pode reduzir os padrões Moiré.

```python
fig, ax = plt.subplots(figsize=(6.8, 6.8))
ax.imshow(a, interpolation='antialiased', cmap='gray')
ax.set_title("upsampled by factor a 1.048, interpolation='antialiased'")
plt.show()
```
