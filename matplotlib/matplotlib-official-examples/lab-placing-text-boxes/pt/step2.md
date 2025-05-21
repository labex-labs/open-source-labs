# Criando um Histograma Básico

Agora que temos nossos dados, vamos criar um histograma para visualizar sua distribuição. Um histograma divide os dados em bins (intervalos) e mostra a frequência de pontos de dados dentro de cada bin.

## Criando o Histograma

Em uma nova célula no seu Jupyter Notebook, insira e execute o seguinte código:

```python
# Create a figure and axes
fig, ax = plt.subplots(figsize=(10, 6))

# Create a histogram with 50 bins
histogram = ax.hist(x, bins=50, color='skyblue', edgecolor='black')

# Add title and labels
ax.set_title('Distribution of Random Data', fontsize=16)
ax.set_xlabel('Value', fontsize=12)
ax.set_ylabel('Frequency', fontsize=12)

# Display the plot
plt.tight_layout()
plt.show()
```

Ao executar esta célula, você deverá ver um histograma exibindo a distribuição dos seus dados aleatórios. A saída terá a aparência de uma curva em forma de sino (distribuição normal) centrada perto de zero.

## Entendendo o Código

Vamos detalhar o que cada linha do código faz:

1. `fig, ax = plt.subplots(figsize=(10, 6))`: Cria um objeto figura e eixos. O parâmetro `figsize` define o tamanho do gráfico em polegadas (largura, altura).

2. `histogram = ax.hist(x, bins=50, color='skyblue', edgecolor='black')`: Cria um histograma dos nossos dados `x` com 50 bins. Os bins são coloridos em skyblue com bordas pretas.

3. `ax.set_title('Distribution of Random Data', fontsize=16)`: Adiciona um título ao gráfico com um tamanho de fonte de 16.

4. `ax.set_xlabel('Value', fontsize=12)` e `ax.set_ylabel('Frequency', fontsize=12)`: Adicionam rótulos aos eixos x e y com um tamanho de fonte de 12.

5. `plt.tight_layout()`: Ajusta automaticamente o gráfico para caber na área da figura.

6. `plt.show()`: Exibe o gráfico.

O histograma mostra como nossos dados são distribuídos. Como usamos `np.random.randn()`, que gera dados de uma distribuição normal, o histograma tem uma forma de sino centrada em torno de 0. A altura de cada barra representa quantos pontos de dados caem dentro daquele intervalo.
