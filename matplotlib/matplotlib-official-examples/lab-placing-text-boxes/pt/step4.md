# Personalizando a Caixa de Texto

Agora que adicionamos com sucesso uma caixa de texto ao nosso gráfico, vamos explorar várias opções de personalização para torná-la mais visualmente atraente e adequada para diferentes contextos.

## Experimentando com Diferentes Estilos

Vamos criar uma função para facilitar a experimentação com diferentes estilos de caixa de texto. Em uma nova célula, insira e execute o seguinte código:

```python
def plot_with_textbox(boxstyle, facecolor, alpha, position=(0.05, 0.95)):
    """
    Create a histogram with a custom text box.

    Parameters:
    boxstyle (str): Style of the box ('round', 'square', 'round4', etc.)
    facecolor (str): Background color of the box
    alpha (float): Transparency of the box (0-1)
    position (tuple): Position of the box in axes coordinates (x, y)
    """
    # Create figure and plot
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.hist(x, bins=50, color='skyblue', edgecolor='black')

    # Set title and labels
    ax.set_title(f'Text Box Style: {boxstyle}', fontsize=16)
    ax.set_xlabel('Value', fontsize=12)
    ax.set_ylabel('Frequency', fontsize=12)

    # Create text box properties
    box_props = dict(boxstyle=boxstyle, facecolor=facecolor, alpha=alpha)

    # Add text box
    ax.text(position[0], position[1], textstr, transform=ax.transAxes,
            fontsize=14, verticalalignment='top', bbox=box_props)

    plt.tight_layout()
    plt.show()
```

Agora, vamos usar esta função para experimentar diferentes estilos de caixa. Em uma nova célula, insira e execute:

```python
# Try a square box with light green color
plot_with_textbox('square', 'lightgreen', 0.7)

# Try a rounded box with light blue color
plot_with_textbox('round', 'lightblue', 0.5)

# Try a box with extra rounded corners
plot_with_textbox('round4', 'lightyellow', 0.6)

# Try a sawtooth style box
plot_with_textbox('sawtooth', 'lightcoral', 0.4)
```

Ao executar esta célula, você verá quatro gráficos diferentes, cada um com um estilo de caixa de texto diferente.

## Alterando a Posição da Caixa de Texto

A posição de uma caixa de texto pode ser crucial para a visualização. Vamos colocar caixas de texto em diferentes cantos do gráfico. Em uma nova célula, insira e execute:

```python
# Create a figure with a 2x2 grid of subplots
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
axes = axes.flatten()  # Flatten to easily iterate

# Define positions for the four corners
positions = [
    (0.05, 0.95),  # Top left
    (0.95, 0.95),  # Top right
    (0.05, 0.05),  # Bottom left
    (0.95, 0.05)   # Bottom right
]

# Define alignments for each position
alignments = [
    ('top', 'left'),          # Top left
    ('top', 'right'),         # Top right
    ('bottom', 'left'),       # Bottom left
    ('bottom', 'right')       # Bottom right
]

# Corner labels
corner_labels = ['Top Left', 'Top Right', 'Bottom Left', 'Bottom Right']

# Create four plots with text boxes in different corners
for i, ax in enumerate(axes):
    # Plot histogram
    ax.hist(x, bins=50, color='skyblue', edgecolor='black')

    # Set title
    ax.set_title(f'Text Box in {corner_labels[i]}', fontsize=14)

    # Create text box properties
    box_props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)

    # Add text box
    ax.text(positions[i][0], positions[i][1], textstr,
            transform=ax.transAxes, fontsize=12,
            verticalalignment=alignments[i][0],
            horizontalalignment=alignments[i][1],
            bbox=box_props)

plt.tight_layout()
plt.show()
```

Este código cria uma grade 2x2 de histogramas, cada um com uma caixa de texto em um canto diferente.

## Entendendo o Posicionamento da Caixa de Texto

Existem vários parâmetros-chave que controlam o posicionamento da caixa de texto:

1. **Coordenadas de posição**: As coordenadas `(x, y)` determinam onde a caixa de texto é colocada. Ao usar `transform=ax.transAxes`, estas estão em coordenadas de eixos, onde `(0, 0)` é o canto inferior esquerdo e `(1, 1)` é o canto superior direito.

2. **Alinhamento vertical**: O parâmetro `verticalalignment` controla como o texto é alinhado verticalmente em relação à coordenada y:
   - `'top'`: A parte superior do texto está na coordenada y especificada.
   - `'center'`: O centro do texto está na coordenada y especificada.
   - `'bottom'`: A parte inferior do texto está na coordenada y especificada.

3. **Alinhamento horizontal**: O parâmetro `horizontalalignment` controla como o texto é alinhado horizontalmente em relação à coordenada x:
   - `'left'`: A borda esquerda do texto está na coordenada x especificada.
   - `'center'`: O centro do texto está na coordenada x especificada.
   - `'right'`: A borda direita do texto está na coordenada x especificada.

Essas opções de alinhamento são particularmente importantes ao colocar texto nos cantos. Por exemplo, no canto superior direito, você gostaria de usar `horizontalalignment='right'` para que a borda direita do texto se alinhe com a borda direita do gráfico.
