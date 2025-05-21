# Criando um Gráfico de Barras com Valor Alfa Uniforme

Neste passo, criaremos um gráfico de barras onde todas as barras têm o mesmo nível de transparência usando o argumento de palavra-chave `alpha`.

## Adicionando uma Nova Célula

Adicione uma nova célula ao seu Jupyter Notebook clicando no botão "+" na barra de ferramentas ou pressionando "Esc" seguido de "b" no modo de comando.

## Criando o Gráfico de Barras com Alfa Uniforme

Insira e execute o seguinte código na nova célula:

```python
import matplotlib.pyplot as plt
import numpy as np

# Set a random seed for reproducibility
np.random.seed(19680801)

# Create a figure and an axes
fig, ax = plt.subplots(figsize=(10, 6))

# Generate data
x_values = list(range(20))  # 0 to 19
y_values = np.random.randn(20)  # 20 random values from standard normal distribution

# Determine bar colors based on y-values (green for positive, red for negative)
facecolors = ['green' if y > 0 else 'red' for y in y_values]
edgecolors = facecolors  # Same color for edges

# Create the bar chart with alpha=0.5 for all bars
ax.bar(x_values, y_values, color=facecolors, edgecolor=edgecolors, alpha=0.5)

# Add a title and labels
ax.set_title("Bar Chart with Uniform Alpha Value (alpha=0.5)")
ax.set_xlabel("X Values")
ax.set_ylabel("Y Values")

# Add a grid for better readability
ax.grid(True, linestyle='--', alpha=0.7)

# Show the plot
plt.show()
```

## Compreendendo o Código e a Saída

Após executar o código, você deve ver um gráfico de barras com 20 barras. Cada barra é verde (valor y positivo) ou vermelha (valor y negativo) com o mesmo nível de transparência (alpha=0.5).

Vamos detalhar as partes principais:

1. `np.random.seed(19680801)` - Isso garante que os números aleatórios gerados sejam os mesmos toda vez que você executar o código.

2. `x_values = list(range(20))` - Cria uma lista de inteiros de 0 a 19 para o eixo x.

3. `y_values = np.random.randn(20)` - Gera 20 valores aleatórios de uma distribuição normal padrão para o eixo y.

4. `facecolors = ['green' if y > 0 else 'red' for y in y_values]` - Esta compreensão de lista atribui verde aos valores positivos e vermelho aos valores negativos.

5. `ax.bar(..., alpha=0.5)` - A parte chave que define um valor alfa uniforme de 0.5 para todas as barras.

O valor alfa uniforme torna todas as barras igualmente transparentes, o que pode ser útil quando você deseja:

- Mostrar linhas de grade de fundo através das barras
- Criar uma visualização mais sutil
- Reduzir o domínio visual de todos os elementos igualmente

No próximo passo, exploraremos como definir diferentes valores alfa para diferentes barras.
