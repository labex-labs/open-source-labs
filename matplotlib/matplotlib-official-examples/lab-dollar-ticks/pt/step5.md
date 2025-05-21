# Salvando o Gráfico e Criando uma Função Reutilizável

Nesta etapa final, criaremos uma função reutilizável para gerar gráficos formatados com moeda e salvar nossa visualização em um arquivo. Essa abordagem facilita a aplicação da mesma formatação a diferentes conjuntos de dados financeiros no futuro.

Em uma nova célula no seu notebook, adicione e execute o seguinte código:

```python
def create_currency_plot(x_data, y_data, title='Financial Data',
                         xlabel='X-Axis', ylabel='Amount ($)',
                         filename=None, show_stats=True):
    """
    Create a plot with currency formatting on the y-axis.

    Parameters:
    -----------
    x_data : array-like
        Data for the x-axis
    y_data : array-like
        Data for the y-axis (currency values)
    title : str
        Title of the plot
    xlabel : str
        Label for the x-axis
    ylabel : str
        Label for the y-axis
    filename : str, optional
        If provided, save the plot to this filename
    show_stats : bool
        Whether to show statistics (average, min, max)

    Returns:
    --------
    fig, ax : tuple
        The figure and axes objects
    """
    # Import the necessary module for formatting
    import matplotlib.ticker as ticker

    # Create a figure and axes
    fig, ax = plt.subplots(figsize=(12, 7))

    # Plot the data
    ax.plot(x_data, y_data, marker='o', linestyle='-', color='blue',
            linewidth=2, markersize=6, label='Data')

    if show_stats:
        # Calculate statistics
        avg_value = np.mean(y_data)
        max_value = np.max(y_data)
        min_value = np.min(y_data)
        max_x = x_data[np.argmax(y_data)]
        min_x = x_data[np.argmin(y_data)]

        # Add a horizontal line for average value
        ax.axhline(y=avg_value, color='r', linestyle='--', alpha=0.7,
                   label=f'Average: ${avg_value:.2f}')

        # Add annotations for max and min values
        ax.annotate(f'Max: ${max_value:.2f}', xy=(max_x, max_value),
                    xytext=(max_x+1, max_value+200),
                    arrowprops=dict(facecolor='black', shrink=0.05, width=1.5))

        ax.annotate(f'Min: ${min_value:.2f}', xy=(min_x, min_value),
                    xytext=(min_x+1, min_value-200),
                    arrowprops=dict(facecolor='black', shrink=0.05, width=1.5))

    # Format y-axis with dollar signs
    formatter = ticker.StrMethodFormatter('${x:,.2f}')
    ax.yaxis.set_major_formatter(formatter)

    # Customize tick parameters
    ax.tick_params(axis='both', which='major', labelsize=10)

    # Add labels and title
    ax.set_xlabel(xlabel, fontsize=12)
    ax.set_ylabel(ylabel, fontsize=12)
    ax.set_title(title, fontsize=14, fontweight='bold')

    # Add grid for better readability
    ax.grid(True, linestyle='--', alpha=0.7)

    # Add legend
    if show_stats:
        ax.legend(loc='best', fontsize=10)

    # Adjust layout
    plt.tight_layout()

    # Save the plot if filename is provided
    if filename:
        plt.savefig(filename, dpi=300, bbox_inches='tight')
        print(f"Plot saved as '{filename}'")

    return fig, ax

# Use our function to create and save a plot
fig, ax = create_currency_plot(
    days,
    daily_revenue,
    title='Monthly Revenue Report',
    xlabel='Day of Month',
    ylabel='Daily Revenue ($)',
    filename='revenue_plot.png'
)

# Display the plot
plt.show()

print("Function created and plot saved successfully!")
```

Após executar este código, você deverá ver:

1. Um gráfico semelhante ao que criamos na etapa anterior, mas gerado usando nossa função personalizada
2. Uma mensagem confirmando que o gráfico foi salvo em um arquivo chamado `revenue_plot.png`

A função que criamos:

- Aceita dados para os eixos x e y
- Permite a personalização de rótulos e título
- Tem uma opção para salvar o gráfico em um arquivo
- Pode mostrar ou ocultar estatísticas como média, mínimo e máximo
- Retorna os objetos de figura e eixos para personalização adicional, se necessário

Essa função reutilizável facilita a criação de gráficos financeiros formatados de forma consistente no futuro. Você pode simplesmente chamar essa função com diferentes conjuntos de dados, e ela tratará toda a formatação de moeda e anotações estatísticas automaticamente.

Para verificar se nosso gráfico foi salvo corretamente, vamos verificar se o arquivo existe:

```python
import os
if os.path.exists('revenue_plot.png'):
    print("Plot file exists! Size:", os.path.getsize('revenue_plot.png'), "bytes")
else:
    print("Plot file was not saved correctly.")
```

Você deverá ver uma mensagem confirmando que o arquivo existe e seu tamanho.

Parabéns! Você aprendeu com sucesso como formatar gráficos com sinais de dólar e criar visualizações financeiras com aparência profissional usando Matplotlib.
