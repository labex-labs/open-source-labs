# Adicionando os Toques Finais ao Gráfico com Eixo Quebrado

Nesta etapa final, adicionaremos os toques finais ao nosso gráfico com eixo quebrado para deixar claro que o eixo y está quebrado. Adicionaremos linhas diagonais entre os _subplots_ para indicar a quebra e melhoraremos a aparência geral do gráfico com rótulos adequados e uma grade.

## Adicionando Linhas Diagonais de Quebra

Para indicar visualmente que o eixo está quebrado, adicionaremos linhas diagonais entre os dois _subplots_. Esta é uma convenção comum que ajuda os espectadores a entender que alguma parte do eixo foi omitida.

Crie uma nova célula e adicione o seguinte código:

```python
# Create two subplots stacked vertically with shared x-axis
fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, figsize=(8, 6))

# Plot the same data on both axes
ax1.plot(pts, 'o-', color='blue')
ax2.plot(pts, 'o-', color='blue')

# Set y-axis limits for each subplot
ax1.set_ylim(0.78, 1.0)    # Top subplot shows only the outliers
ax2.set_ylim(0, 0.22)      # Bottom subplot shows only the main data

# Hide the spines between ax1 and ax2
ax1.spines.bottom.set_visible(False)
ax2.spines.top.set_visible(False)

# Adjust the position of the ticks
ax1.xaxis.tick_top()          # Move x-axis ticks to the top
ax1.tick_params(labeltop=False)  # Hide x-axis tick labels at the top
ax2.xaxis.tick_bottom()       # Keep x-axis ticks at the bottom

# Add diagonal break lines
d = 0.5  # proportion of vertical to horizontal extent of the slanted line
kwargs = dict(marker=[(-1, -d), (1, d)], markersize=12,
              linestyle='none', color='k', mec='k', mew=1, clip_on=False)
ax1.plot([0, 1], [0, 0], transform=ax1.transAxes, **kwargs)
ax2.plot([0, 1], [1, 1], transform=ax2.transAxes, **kwargs)

# Add labels and a title
ax2.set_xlabel('Data Point Index')
ax2.set_ylabel('Value')
ax1.set_ylabel('Value')
fig.suptitle('Dataset with Outliers', fontsize=16)

# Add a grid to both subplots for better readability
ax1.grid(True, linestyle='--', alpha=0.7)
ax2.grid(True, linestyle='--', alpha=0.7)

plt.tight_layout()
plt.subplots_adjust(hspace=0.1)  # Adjust the space between subplots
plt.show()
```

Ao executar esta célula, você deverá ver o gráfico completo com eixo quebrado com linhas diagonais indicando a quebra no eixo y. O gráfico agora tem um título, rótulos de eixo e linhas de grade para melhorar a legibilidade.

## Entendendo o Gráfico com Eixo Quebrado

Vamos dedicar um momento para entender os componentes-chave do nosso gráfico com eixo quebrado:

1.  **Dois _Subplots_**: Criamos dois _subplots_ separados, cada um focado em um intervalo diferente de valores y.
2.  **_Spines_ Ocultas**: Ocultamos as _spines_ de conexão entre os _subplots_ para criar uma separação visual.
3.  **Linhas Diagonais de Quebra**: Adicionamos linhas diagonais para indicar que o eixo está quebrado.
4.  **Limites do Eixo Y**: Definimos limites diferentes para o eixo y para cada _subplot_ para focar em partes específicas dos dados.
5.  **Linhas de Grade**: Adicionamos linhas de grade para melhorar a legibilidade e facilitar a estimativa de valores.

Esta técnica é especialmente útil quando você tem _outliers_ em seus dados que, de outra forma, comprimiriam a visualização da maioria dos seus pontos de dados. Ao "quebrar" o eixo, você pode mostrar tanto os _outliers_ quanto a distribuição principal dos dados claramente em uma única figura.

## Experimentando com o Gráfico

Agora que você entende como criar um gráfico com eixo quebrado, pode experimentar diferentes configurações. Tente alterar os limites do eixo y, adicionar mais recursos ao gráfico ou aplicar esta técnica aos seus próprios dados.

Por exemplo, você pode modificar o código anterior para incluir uma legenda, alterar o esquema de cores ou ajustar os estilos dos marcadores:

```python
# Create two subplots stacked vertically with shared x-axis
fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, figsize=(8, 6))

# Plot the same data on both axes with different styles
ax1.plot(pts, 'o-', color='darkblue', label='Data Points', linewidth=2)
ax2.plot(pts, 'o-', color='darkblue', linewidth=2)

# Mark the outliers with a different color
outlier_indices = [3, 14]
ax1.plot(outlier_indices, pts[outlier_indices], 'ro', markersize=8, label='Outliers')

# Set y-axis limits for each subplot
ax1.set_ylim(0.78, 1.0)    # Top subplot shows only the outliers
ax2.set_ylim(0, 0.22)      # Bottom subplot shows only the main data

# Hide the spines between ax1 and ax2
ax1.spines.bottom.set_visible(False)
ax2.spines.top.set_visible(False)

# Adjust the position of the ticks
ax1.xaxis.tick_top()          # Move x-axis ticks to the top
ax1.tick_params(labeltop=False)  # Hide x-axis tick labels at the top
ax2.xaxis.tick_bottom()       # Keep x-axis ticks at the bottom

# Add diagonal break lines
d = 0.5  # proportion of vertical to horizontal extent of the slanted line
kwargs = dict(marker=[(-1, -d), (1, d)], markersize=12,
              linestyle='none', color='k', mec='k', mew=1, clip_on=False)
ax1.plot([0, 1], [0, 0], transform=ax1.transAxes, **kwargs)
ax2.plot([0, 1], [1, 1], transform=ax2.transAxes, **kwargs)

# Add labels and a title
ax2.set_xlabel('Data Point Index')
ax2.set_ylabel('Value')
ax1.set_ylabel('Value')
fig.suptitle('Dataset with Outliers - Enhanced Visualization', fontsize=16)

# Add a grid to both subplots for better readability
ax1.grid(True, linestyle='--', alpha=0.7)
ax2.grid(True, linestyle='--', alpha=0.7)

# Add a legend to the top subplot
ax1.legend(loc='upper right')

plt.tight_layout()
plt.subplots_adjust(hspace=0.1)  # Adjust the space between subplots
plt.show()
```

Ao executar este código aprimorado, você deverá ver uma visualização aprimorada com _outliers_ marcados especificamente e uma legenda explicando os pontos de dados.

Parabéns! Você criou com sucesso um gráfico com eixo quebrado em Python usando Matplotlib. Esta técnica o ajudará a criar visualizações mais eficazes ao lidar com dados que contêm _outliers_.
