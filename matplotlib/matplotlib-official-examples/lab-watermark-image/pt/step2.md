# Carregando e Examinando a Imagem

Agora que importamos as nossas bibliotecas, precisamos carregar a imagem que queremos sobrepor no nosso gráfico. O Matplotlib fornece algumas imagens de exemplo que podemos usar para praticar.

1. Crie uma nova célula no seu notebook e insira o seguinte código:

```python
# Load the sample image
with cbook.get_sample_data('logo2.png') as file:
    im = image.imread(file)

# Display information about the image
print(f"Image shape: {im.shape}")
print(f"Image data type: {im.dtype}")

# Display the image
plt.figure(figsize=(4, 4))
plt.imshow(im)
plt.axis('off')  # Hide axis
plt.title('Matplotlib Logo')
plt.show()
```

Este código faz o seguinte:

- Usa `cbook.get_sample_data()` para carregar uma imagem de exemplo chamada 'logo2.png' da coleção de dados de exemplo do Matplotlib.
- Usa `image.imread()` para ler o ficheiro de imagem num array NumPy.
- Imprime informações sobre as dimensões e o tipo de dados da imagem.
- Cria uma figura e exibe a imagem usando `plt.imshow()`.
- Oculta as marcas e rótulos dos eixos com `plt.axis('off')`.
- Adiciona um título à figura.
- Exibe a figura usando `plt.show()`.

2. Execute a célula pressionando Shift+Enter.

A saída deve exibir informações sobre a imagem e mostrar o logótipo do Matplotlib. A forma da imagem indica as dimensões da imagem (altura, largura, canais de cor), e o tipo de dados informa-nos como os dados da imagem são armazenados.

![image-info](../assets/screenshot-20250306-cqkw4mpg@2x.png)

Este passo é importante porque nos ajuda a entender a imagem que usaremos como sobreposição. Podemos ver a sua aparência e dimensões, o que será útil ao decidir como posicioná-la no nosso gráfico.
