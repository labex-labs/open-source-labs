# Examinando Intervalos de Dados Específicos

Às vezes, pode ser necessário examinar intervalos de dados específicos em uma imagem. Podemos fazer isso ajustando os limites do mapa de cores (colormap) usando o parâmetro `clim` na função `imshow`. Isso nos permite focar em regiões específicas da imagem, sacrificando detalhes em outras regiões.

```python
min_value, max_value = 100, 200
plt.imshow(img, clim=(min_value, max_value))
```
