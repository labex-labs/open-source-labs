# Posicionamento Avançado de Títulos com Subplots

Nesta etapa, você aprenderá técnicas avançadas para o posicionamento de títulos ao trabalhar com layouts de subplot e objetos de eixos. Você também aprenderá como usar a função `suptitle()` para adicionar um título geral a uma figura com vários subplots.

## Criando uma Figura com Subplots e Títulos Individuais

Vamos criar uma grade 2x2 de subplots, cada um com seu próprio título posicionado de forma diferente:

```python
# Create a figure with a 2x2 grid of subplots
fig, axes = plt.subplots(2, 2, figsize=(10, 8))

# Flatten the 2D array of axes for easier iteration
axes = axes.flatten()

# Plot data and set titles with different positions for each subplot
for i, ax in enumerate(axes):
    ax.plot(range(10))
    ax.grid(True)

# Top-left subplot: Default centered title
axes[0].set_title('Default (Centered)')

# Top-right subplot: Left-aligned title
axes[1].set_title('Left-Aligned', loc='left')

# Bottom-left subplot: Right-aligned title
axes[2].set_title('Right-Aligned', loc='right')

# Bottom-right subplot: Custom positioned title
axes[3].set_title('Custom Position', y=0.85, loc='center')

# Add spacing between subplots
plt.tight_layout()
plt.show()
```

Execute a célula. Você deve ver quatro subplots, cada um com um título posicionado de forma diferente.

## Adicionando um Título em Nível de Figura com suptitle()

Ao trabalhar com vários subplots, você pode querer adicionar um título geral para toda a figura. Isso pode ser feito usando a função `suptitle()`:

```python
# Create a figure with a 2x2 grid of subplots
fig, axes = plt.subplots(2, 2, figsize=(10, 8))

# Flatten the 2D array of axes for easier iteration
axes = axes.flatten()

# Plot data on each subplot
for i, ax in enumerate(axes):
    ax.plot(range(10))
    ax.grid(True)
    ax.set_title(f'Subplot {i+1}')

# Add an overall title to the figure
fig.suptitle('Multiple Subplots with an Overall Title', fontsize=16)

# Add spacing between subplots
plt.tight_layout()
# Add top spacing for the suptitle
plt.subplots_adjust(top=0.9)
plt.show()
```

Execute a célula. Você deve ver quatro subplots, cada um com seu próprio título, e um título geral para a figura no topo.

## Combinando Títulos de Eixos e Títulos de Figura

Você pode combinar títulos de subplot individuais com um título geral da figura:

```python
# Create a figure with a 2x2 grid of subplots
fig, axes = plt.subplots(2, 2, figsize=(10, 8))

# Plot data on each subplot with different title positions
axes[0, 0].plot(range(10))
axes[0, 0].grid(True)
axes[0, 0].set_title('Centered Title', loc='center')

axes[0, 1].plot(range(10))
axes[0, 1].grid(True)
axes[0, 1].set_title('Left-Aligned Title', loc='left')

axes[1, 0].plot(range(10))
axes[1, 0].grid(True)
axes[1, 0].set_title('Right-Aligned Title', loc='right')

axes[1, 1].plot(range(10))
axes[1, 1].grid(True)
axes[1, 1].set_title('Lower Title', y=0.85)

# Add an overall title to the figure
fig.suptitle('Advanced Title Positioning Demo', fontsize=16)

# Add spacing between subplots
plt.tight_layout()
# Add top spacing for the suptitle
plt.subplots_adjust(top=0.9)
plt.show()
```

Execute a célula. Você deve ver uma figura com quatro subplots, cada um com um título posicionado de forma diferente, e um título geral no topo da figura.

A função `suptitle()` é útil para adicionar um título principal que descreve toda a figura, enquanto as chamadas individuais `set_title()` nos objetos de eixos adicionam títulos mais específicos a cada subplot.
