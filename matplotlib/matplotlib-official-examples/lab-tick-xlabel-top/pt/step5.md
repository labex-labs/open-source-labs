# Salvando e Compartilhando Seu Gráfico

A etapa final é salvar seu gráfico personalizado para que você possa incluí-lo em relatórios, apresentações ou compartilhá-lo com outras pessoas.

## Salvando Gráficos em Diferentes Formatos

O Matplotlib permite que você salve gráficos em vários formatos, incluindo PNG, JPG, PDF, SVG e muito mais. Vamos aprender como salvar nosso gráfico em diferentes formatos:

```python
# Create a plot similar to our previous customized one
fig, ax = plt.subplots(figsize=(10, 6))

# Generate data
x = np.linspace(0, 2*np.pi, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Plot the data
ax.plot(x, y1, linewidth=2, color='blue', label='sin(x)')
ax.plot(x, y2, linewidth=2, color='red', label='cos(x)')

# Move the x-axis tick labels to the top
ax.tick_params(
    axis='x',
    top=True,
    labeltop=True,
    bottom=False,
    labelbottom=False
)

# Customize tick labels
ax.set_xticks(np.arange(0, 2*np.pi + 0.1, np.pi/2))
ax.set_xticklabels(['0', 'π/2', 'π', '3π/2', '2π'])

# Add title and labels
ax.set_title('Plot with X-Axis Labels at the Top', fontsize=14)
ax.set_xlabel('X-axis at the top')
ax.set_ylabel('Y-axis')

# Add grid and legend
ax.grid(True)
ax.legend()

# Save the figure in different formats
plt.savefig('plot_with_top_xlabels.png', dpi=300, bbox_inches='tight')
plt.savefig('plot_with_top_xlabels.pdf', bbox_inches='tight')
plt.savefig('plot_with_top_xlabels.svg', bbox_inches='tight')

# Show the plot
plt.show()

print("The plot has been saved in PNG, PDF, and SVG formats in the current directory.")
```

Ao executar este código, o gráfico será salvo em três formatos diferentes:

- PNG: Um formato de imagem raster bom para a web e uso geral
- PDF: Um formato vetorial ideal para publicações e relatórios
- SVG: Um formato vetorial excelente para web e gráficos editáveis

Os arquivos serão salvos no diretório de trabalho atual do seu notebook Jupyter.

## Entendendo os Parâmetros de Salvamento

Vamos examinar os parâmetros usados com `savefig()`:

- `dpi=300`: Define a resolução (pontos por polegada) para formatos raster como PNG
- `bbox_inches='tight'`: Ajusta automaticamente os limites da figura para incluir todos os elementos sem espaço em branco desnecessário

## Visualizando os Arquivos Salvos

Você pode visualizar os arquivos salvos navegando no navegador de arquivos no Jupyter:

1. Clique no logotipo "Jupyter" no canto superior esquerdo
2. No navegador de arquivos, você deve ver os arquivos de imagem salvos
3. Clique em qualquer arquivo para visualizá-lo ou baixá-lo

## Opções Adicionais de Exportação de Gráficos

Para ter mais controle sobre o gráfico salvo, você pode personalizar o tamanho da figura, ajustar o fundo ou alterar o DPI de acordo com suas necessidades:

```python
# Control the background color and transparency
fig.patch.set_facecolor('white')  # Set figure background color
fig.patch.set_alpha(0.8)          # Set background transparency

# Save with custom settings
plt.savefig('custom_background_plot.png',
            dpi=400,              # Higher resolution
            facecolor=fig.get_facecolor(),  # Use the figure's background color
            edgecolor='none',     # No edge color
            bbox_inches='tight',  # Tight layout
            pad_inches=0.1)       # Add a small padding

print("A customized plot has been saved with specialized export settings.")
```

Isso demonstra como salvar gráficos com controle preciso sobre o formato e a aparência da saída.
