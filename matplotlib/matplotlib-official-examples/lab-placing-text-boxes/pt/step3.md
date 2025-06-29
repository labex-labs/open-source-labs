# Adicionando uma Caixa de Texto com Estatísticas

Agora que temos um histograma básico, vamos aprimorá-lo adicionando uma caixa de texto que exibe as informações estatísticas sobre nossos dados. Isso tornará a visualização mais informativa para os espectadores.

## Criando o Conteúdo do Texto

Primeiro, precisamos preparar o conteúdo do texto que irá dentro da nossa caixa de texto. Em uma nova célula, insira e execute o seguinte código:

```python
# Create a string with the statistics
textstr = '\n'.join((
    r'$\mu=%.2f$' % (mu,),           # Mean
    r'$\mathrm{median}=%.2f$' % (median,),  # Median
    r'$\sigma=%.2f$' % (sigma,)       # Standard deviation
))

print("Text content for our box:")
print(textstr)
```

Você deverá ver uma saída semelhante a:

```
Text content for our box:
$\mu=-0.31$
$\mathrm{median}=-0.28$
$\sigma=29.86$
```

Este código cria uma string de várias linhas contendo a média, a mediana e o desvio padrão dos nossos dados. Vamos examinar alguns aspectos interessantes deste código:

1. O método `\n'.join(...)` junta várias strings com um caractere de nova linha entre elas.
2. O `r` antes de cada string a torna uma string "raw", o que é útil ao incluir caracteres especiais.
3. A notação `$...$` é usada para formatação matemática no estilo LaTeX em matplotlib.
4. `\mu` e `\sigma` são símbolos LaTeX para as letras gregas μ (mu) e σ (sigma).
5. `%.2f` é um especificador de formatação que exibe um número de ponto flutuante com duas casas decimais.

## Criando e Adicionando a Caixa de Texto

Agora, vamos recriar nosso histograma e adicionar a caixa de texto a ele. Em uma nova célula, insira e execute o seguinte código:

```python
# Create a new figure and axes
fig, ax = plt.subplots(figsize=(10, 6))

# Create a histogram with 50 bins
histogram = ax.hist(x, bins=50, color='skyblue', edgecolor='black')

# Add title and labels
ax.set_title('Distribution of Random Data with Statistics', fontsize=16)
ax.set_xlabel('Value', fontsize=12)
ax.set_ylabel('Frequency', fontsize=12)

# Define the properties of the text box
properties = dict(boxstyle='round', facecolor='wheat', alpha=0.5)

# Add the text box to the plot
# Position the box in the top left corner (0.05, 0.95) in axes coordinates
ax.text(0.05, 0.95, textstr, transform=ax.transAxes, fontsize=14,
        verticalalignment='top', bbox=properties)

# Display the plot
plt.tight_layout()
plt.show()
```

Ao executar esta célula, você deverá ver seu histograma com uma caixa de texto no canto superior esquerdo exibindo as estatísticas.

## Entendendo o Código da Caixa de Texto

Vamos detalhar as partes importantes do código que criam a caixa de texto:

1. `properties = dict(boxstyle='round', facecolor='wheat', alpha=0.5)`:
   - Isso cria um dicionário com propriedades para a caixa de texto.
   - `boxstyle='round'`: Faz com que a caixa tenha cantos arredondados.
   - `facecolor='wheat'`: Define a cor de fundo da caixa para trigo.
   - `alpha=0.5`: Torna a caixa semi-transparente (50% de opacidade).

2. `ax.text(0.05, 0.95, textstr, transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=properties)`:
   - Isso adiciona texto aos eixos na posição (0.05, 0.95).
   - `transform=ax.transAxes`: Isso é crucial - significa que as coordenadas estão em unidades de eixos (0-1) em vez de unidades de dados. Portanto, (0.05, 0.95) significa "5% da borda esquerda e 95% da borda inferior do gráfico."
   - `fontsize=14`: Define o tamanho da fonte.
   - `verticalalignment='top'`: Alinha o texto para que a parte superior do texto esteja na coordenada y especificada.
   - `bbox=properties`: Aplica nossas propriedades da caixa de texto.

A caixa de texto permanecerá na mesma posição em relação aos eixos do gráfico, mesmo que você amplie o gráfico ou altere a faixa de dados. Isso ocorre porque usamos `transform=ax.transAxes`, que usa coordenadas de eixos em vez de coordenadas de dados.
