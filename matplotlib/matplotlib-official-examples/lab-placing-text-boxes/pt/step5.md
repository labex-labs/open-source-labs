# Criando uma Visualização Final com Múltiplos Elementos de Texto

Nesta etapa final, combinaremos tudo o que aprendemos para criar uma visualização abrangente que inclui múltiplos elementos de texto com diferentes estilos. Isso demonstrará como as caixas de texto podem ser usadas para aprimorar a narrativa de dados.

## Criando uma Visualização Avançada

Vamos criar um gráfico mais sofisticado que inclua nosso histograma e alguns elementos visuais adicionais. Em uma nova célula, insira e execute o seguinte código:

```python
# Create a figure with a larger size for our final visualization
fig, ax = plt.subplots(figsize=(12, 8))

# Plot the histogram with more bins and a different color
n, bins, patches = ax.hist(x, bins=75, color='lightblue',
                           edgecolor='darkblue', alpha=0.7)

# Add title and labels with improved styling
ax.set_title('Distribution of Random Data with Statistical Annotations',
             fontsize=18, fontweight='bold', pad=20)
ax.set_xlabel('Value', fontsize=14)
ax.set_ylabel('Frequency', fontsize=14)

# Add grid for better readability
ax.grid(True, linestyle='--', alpha=0.7)

# Mark the mean with a vertical line
ax.axvline(x=mu, color='red', linestyle='-', linewidth=2,
           label=f'Mean: {mu:.2f}')

# Mark one standard deviation range
ax.axvline(x=mu + sigma, color='green', linestyle='--', linewidth=1.5,
           label=f'Mean + 1σ: {mu+sigma:.2f}')
ax.axvline(x=mu - sigma, color='green', linestyle='--', linewidth=1.5,
           label=f'Mean - 1σ: {mu-sigma:.2f}')

# Create a text box with statistics in the top left
stats_box_props = dict(boxstyle='round', facecolor='lightyellow',
                      alpha=0.8, edgecolor='gold', linewidth=2)

stats_text = '\n'.join((
    r'$\mathbf{Statistics:}$',
    r'$\mu=%.2f$ (mean)' % (mu,),
    r'$\mathrm{median}=%.2f$' % (median,),
    r'$\sigma=%.2f$ (std. dev.)' % (sigma,)
))

ax.text(0.05, 0.95, stats_text, transform=ax.transAxes, fontsize=14,
        verticalalignment='top', bbox=stats_box_props)

# Add an informational text box in the top right
info_box_props = dict(boxstyle='round4', facecolor='lightcyan',
                     alpha=0.8, edgecolor='deepskyblue', linewidth=2)

info_text = '\n'.join((
    r'$\mathbf{About\ Normal\ Distributions:}$',
    r'$\bullet\ 68\%\ of\ data\ within\ 1\sigma$',
    r'$\bullet\ 95\%\ of\ data\ within\ 2\sigma$',
    r'$\bullet\ 99.7\%\ of\ data\ within\ 3\sigma$'
))

ax.text(0.95, 0.95, info_text, transform=ax.transAxes, fontsize=14,
        verticalalignment='top', horizontalalignment='right',
        bbox=info_box_props)

# Add a legend
ax.legend(fontsize=12)

# Tighten the layout and show the plot
plt.tight_layout()
plt.show()
```

Ao executar esta célula, você verá uma visualização abrangente com:

- Um histograma dos dados com estilo aprimorado
- Linhas verticais marcando a média e a faixa de um desvio padrão
- Uma caixa de texto de estatísticas no canto superior esquerdo
- Uma caixa de texto informativa sobre distribuições normais no canto superior direito
- Uma legenda explicando as linhas verticais

## Entendendo os Elementos Avançados

Vamos examinar alguns dos novos elementos que adicionamos:

1. **Linhas Verticais com `axvline()`**:
   - Essas linhas marcam estatísticas importantes diretamente no gráfico.
   - O parâmetro `label` permite que essas linhas sejam incluídas na legenda.

2. **Múltiplas Caixas de Texto com Diferentes Estilos**:
   - Cada caixa de texto serve a um propósito diferente e usa um estilo distinto.
   - A caixa de estatísticas mostra os valores calculados a partir de nossos dados.
   - A caixa informativa fornece contexto sobre distribuições normais.

3. **Formatação Aprimorada**:
   - A formatação LaTeX é usada para criar texto em negrito com `\mathbf{}`
   - Marcadores são criados com `\bullet`
   - O espaçamento é controlado com `\ ` (barra invertida seguida de um espaço)

4. **Grade e Legenda**:
   - A grade ajuda os espectadores a ler os valores do gráfico com mais precisão.
   - A legenda explica o significado das linhas coloridas.

## Notas Finais sobre o Posicionamento da Caixa de Texto

Ao colocar múltiplos elementos de texto em uma visualização, considere:

1. **Hierarquia visual**: A informação mais importante deve se destacar mais.
2. **Posicionamento**: Coloque informações relacionadas perto das partes relevantes da visualização.
3. **Contraste**: Certifique-se de que o texto seja legível em relação ao seu fundo.
4. **Consistência**: Use um estilo consistente para tipos semelhantes de informações.
5. **Desordem**: Evite sobrecarregar a visualização com muitos elementos de texto.

Ao colocar e estilizar cuidadosamente as caixas de texto, você pode criar visualizações que são informativas e visualmente atraentes, guiando os espectadores a entender as principais informações de seus dados.
