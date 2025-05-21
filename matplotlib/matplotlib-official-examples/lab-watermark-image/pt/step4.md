# Sobrepondo a Imagem no Gráfico

Agora que criamos o nosso gráfico base, vamos sobrepor a imagem nele. Usaremos o método `figimage` para adicionar a imagem à figura, e torná-la semi-transparente para que o gráfico por baixo permaneça visível.

1. Crie uma nova célula no seu notebook e insira o seguinte código:

```python
# Create a figure and axes for our plot (same as before)
fig, ax = plt.subplots(figsize=(10, 6))

# Set a random seed for reproducibility
np.random.seed(19680801)

# Generate random data
x = np.arange(30)  # x-axis values (0 to 29)
y = x + np.random.randn(30)  # y-axis values (x plus random noise)

# Create a bar chart
bars = ax.bar(x, y, color='#6bbc6b')  # Green bars

# Add grid lines
ax.grid(linestyle='--', alpha=0.7)

# Add labels and title
ax.set_xlabel('X-axis Label')
ax.set_ylabel('Y-axis Label')
ax.set_title('Bar Chart with Image Overlay')

# Load the image
with cbook.get_sample_data('logo2.png') as file:
    im = image.imread(file)

# Overlay the image on the plot
# Parameters:
# - im: the image data
# - 25, 25: x and y position in pixels from the bottom left
# - zorder=3: controls the drawing order (higher numbers are drawn on top)
# - alpha=0.5: controls the transparency (0 = transparent, 1 = opaque)
fig.figimage(im, 25, 25, zorder=3, alpha=0.5)

# Display the plot
plt.tight_layout()
plt.show()
```

Este código combina o que fizemos nos passos anteriores e adiciona o método `figimage` para sobrepor a nossa imagem no gráfico. Aqui está uma análise dos parâmetros `figimage`:

- `im`: Os dados da imagem como um array NumPy.
- `25, 25`: As posições x e y em pixels a partir do canto inferior esquerdo da figura.
- `zorder=3`: Controla a ordem de desenho. Números mais altos são desenhados em cima de elementos com números mais baixos.
- `alpha=0.5`: Controla a transparência da imagem. Um valor de 0 é completamente transparente, e 1 é completamente opaco.

2. Execute a célula pressionando Shift+Enter.

A saída deve mostrar o mesmo gráfico de barras de antes, mas agora com o logótipo do Matplotlib sobreposto no canto inferior esquerdo. O logótipo deve ser semi-transparente, permitindo que o gráfico por baixo permaneça visível.

3. Vamos experimentar com diferentes posições e níveis de transparência. Crie uma nova célula e insira o seguinte código:

```python
# Create a figure and axes for our plot
fig, ax = plt.subplots(figsize=(10, 6))

# Set a random seed for reproducibility
np.random.seed(19680801)

# Generate random data
x = np.arange(30)
y = x + np.random.randn(30)

# Create a bar chart
bars = ax.bar(x, y, color='#6bbc6b')
ax.grid(linestyle='--', alpha=0.7)
ax.set_xlabel('X-axis Label')
ax.set_ylabel('Y-axis Label')
ax.set_title('Bar Chart with Centered Image Overlay')

# Load the image
with cbook.get_sample_data('logo2.png') as file:
    im = image.imread(file)

# Get figure dimensions
fig_width, fig_height = fig.get_size_inches() * fig.dpi

# Calculate center position (this is approximate)
x_center = fig_width / 2 - im.shape[1] / 2
y_center = fig_height / 2 - im.shape[0] / 2

# Overlay the image at the center with higher transparency
fig.figimage(im, x_center, y_center, zorder=3, alpha=0.3)

# Display the plot
plt.tight_layout()
plt.show()
```

Este código coloca a imagem no centro da figura com um nível de transparência mais alto (alpha=0.3), tornando-a mais adequada como uma marca d'água.

4. Execute a célula pressionando Shift+Enter.

A saída deve mostrar o gráfico de barras com o logótipo centrado e mais transparente do que antes, criando um efeito de marca d'água.
