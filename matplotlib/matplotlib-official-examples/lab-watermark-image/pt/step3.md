# Criando um Gráfico Básico com Dados Aleatórios

Antes de adicionarmos a sobreposição da nossa imagem, precisamos criar um gráfico que servirá como base para a nossa visualização. Vamos criar um gráfico de barras simples usando dados aleatórios.

1. Crie uma nova célula no seu notebook e insira o seguinte código:

```python
# Create a figure and axes for our plot
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
ax.set_title('Bar Chart with Random Data')

# Display the plot
plt.tight_layout()
plt.show()
```

Este código faz o seguinte:

- Cria uma figura e eixos com um tamanho específico usando `plt.subplots()`.
- Define uma semente aleatória para garantir que obtemos os mesmos valores aleatórios cada vez que executamos o código.
- Gera 30 valores x (0 a 29) e os correspondentes valores y (x mais ruído aleatório).
- Cria um gráfico de barras com barras verdes usando `ax.bar()`.
- Adiciona linhas de grade ao gráfico com `ax.grid()`.
- Adiciona rótulos para o eixo x, eixo y e um título para o gráfico.
- Usa `plt.tight_layout()` para ajustar o espaçamento para uma melhor aparência.
- Exibe o gráfico usando `plt.show()`.

2. Execute a célula pressionando Shift+Enter.

A saída deve exibir um gráfico de barras com barras verdes representando os dados aleatórios. O eixo x mostra inteiros de 0 a 29, e o eixo y mostra os valores correspondentes com ruído aleatório adicionado.

Este gráfico será a base sobre a qual sobreporemos a nossa imagem no próximo passo. Observe como armazenamos o objeto figura na variável `fig` e o objeto eixos na variável `ax`. Precisaremos dessas variáveis para adicionar a sobreposição da nossa imagem.
