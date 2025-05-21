# Criando uma Função Reutilizável para Sobreposições de Imagens

Para tornar o nosso código mais reutilizável, vamos criar uma função que pode adicionar uma sobreposição de imagem a qualquer figura do Matplotlib. Desta forma, podemos facilmente aplicar o mesmo efeito a diferentes gráficos.

1. Crie uma nova célula no seu notebook e insira o seguinte código:

```python
def add_image_overlay(fig, image_path, x_pos=25, y_pos=25, alpha=0.5, zorder=3):
    """
    Add an image overlay to a matplotlib figure.

    Parameters:
    -----------
    fig : matplotlib.figure.Figure
        The figure to add the image to
    image_path : str
        Path to the image file
    x_pos : int
        X position in pixels from the bottom left
    y_pos : int
        Y position in pixels from the bottom left
    alpha : float
        Transparency level (0 to 1)
    zorder : int
        Drawing order (higher numbers are drawn on top)

    Returns:
    --------
    fig : matplotlib.figure.Figure
        The figure with the image overlay
    """
    # Load the image
    with cbook.get_sample_data(image_path) as file:
        im = image.imread(file)

    # Add the image to the figure
    fig.figimage(im, x_pos, y_pos, zorder=zorder, alpha=alpha)

    return fig

# Example usage: Create a scatter plot with an image overlay
fig, ax = plt.subplots(figsize=(10, 6))

# Set a random seed for reproducibility
np.random.seed(19680801)

# Generate random data for a scatter plot
x = np.random.rand(50) * 10
y = np.random.rand(50) * 10

# Create a scatter plot
ax.scatter(x, y, s=100, c=np.random.rand(50), cmap='viridis', alpha=0.7)
ax.grid(linestyle='--', alpha=0.7)
ax.set_xlabel('X-axis Label')
ax.set_ylabel('Y-axis Label')
ax.set_title('Scatter Plot with Image Overlay')

# Add the image overlay using our function
add_image_overlay(fig, 'logo2.png', x_pos=50, y_pos=50, alpha=0.4)

# Display the plot
plt.tight_layout()
plt.show()
```

Este código define uma função chamada `add_image_overlay` que:

- Recebe parâmetros para a figura, caminho da imagem, posição, transparência e z-order.
- Carrega a imagem especificada.
- Adiciona a imagem à figura usando `figimage`.
- Retorna a figura modificada.

Após definir a função, demonstramos seu uso criando um gráfico de dispersão com dados aleatórios e adicionando o logótipo do Matplotlib como uma sobreposição.

2. Execute a célula pressionando Shift+Enter.

A saída deve mostrar um gráfico de dispersão com pontos posicionados e coloridos aleatoriamente, e o logótipo do Matplotlib sobreposto na posição (50, 50) com 40% de opacidade.

3. Vamos tentar mais um exemplo com um gráfico de linhas. Crie uma nova célula e insira o seguinte código:

```python
# Example usage: Create a line plot with an image overlay
fig, ax = plt.subplots(figsize=(10, 6))

# Generate data for a line plot
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create a line plot
ax.plot(x, y, linewidth=2, color='#d62728')
ax.grid(linestyle='--', alpha=0.7)
ax.set_xlabel('X-axis Label')
ax.set_ylabel('Y-axis Label')
ax.set_title('Sine Wave with Image Overlay')
ax.set_ylim(-1.5, 1.5)

# Add the image overlay using our function
# Place it in the bottom right corner
fig_width, fig_height = fig.get_size_inches() * fig.dpi
with cbook.get_sample_data('logo2.png') as file:
    im = image.imread(file)
    x_pos = fig_width - im.shape[1] - 50  # 50 pixels from the right edge

add_image_overlay(fig, 'logo2.png', x_pos=x_pos, y_pos=50, alpha=0.6)

# Display the plot
plt.tight_layout()
plt.show()
```

Este código cria um gráfico de linhas mostrando uma onda senoidal e adiciona o logótipo do Matplotlib no canto inferior direito do gráfico.

4. Execute a célula pressionando Shift+Enter.

A saída deve mostrar um gráfico de linhas de uma onda senoidal com o logótipo do Matplotlib sobreposto no canto inferior direito com 60% de opacidade.

Estes exemplos demonstram como a nossa função `add_image_overlay` pode ser usada para adicionar facilmente sobreposições de imagem a diferentes tipos de gráficos, tornando-a uma ferramenta versátil para personalizar visualizações.
