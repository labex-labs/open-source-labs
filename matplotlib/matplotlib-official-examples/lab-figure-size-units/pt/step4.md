# Tamanho da Figura em Pixel

Também podemos especificar o tamanho da figura em pixels. Para fazer isso, precisamos converter o valor em pixels para polegadas. Podemos obter o fator de conversão de pixels para polegadas dividindo 1 pelo valor de dpi (dots per inch - pontos por polegada). Em seguida, podemos usar esse valor como o parâmetro `figsize` na função `subplots`. O código abaixo mostra como criar uma figura com um tamanho de 600 pixels x 200 pixels.

```python
px = 1/plt.rcParams['figure.dpi']  # pixel in inches
plt.subplots(figsize=(600*px, 200*px))
plt.show()
```
