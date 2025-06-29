# Criando uma Visualização Combinada com Diferentes Técnicas Alfa

Neste passo final, combinaremos múltiplas técnicas para criar uma visualização mais complexa que demonstra valores alfa uniformes e variáveis em um único gráfico.

## Adicionando uma Nova Célula

Adicione uma nova célula ao seu Jupyter Notebook clicando no botão "+" na barra de ferramentas ou pressionando "Esc" seguido de "b" no modo de comando.

## Criando uma Visualização Combinada

Insira e execute o seguinte código na nova célula:

```python
import matplotlib.pyplot as plt
import numpy as np

# Set a random seed for reproducibility
np.random.seed(19680801)

# Create a figure with two subplots side by side
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Generate some common data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.sin(x) * np.cos(x)

# First subplot: Fixed alpha for all lines
ax1.plot(x, y1, color='red', linewidth=2, label='sin(x)', alpha=0.7)
ax1.plot(x, y2, color='blue', linewidth=2, label='cos(x)', alpha=0.7)
ax1.plot(x, y3, color='green', linewidth=2, label='sin(x)cos(x)', alpha=0.7)

# Add title and legend to first subplot
ax1.set_title("Multiple Lines with Uniform Alpha")
ax1.set_xlabel("x")
ax1.set_ylabel("y")
ax1.legend()
ax1.grid(True, linestyle='--', alpha=0.5)

# Second subplot: Scatter plot with varying alpha based on y-value
sizes = np.abs(y3 * 100) + 10  # Vary point sizes based on y3
colors = y3  # Use y3 values for coloring

# Calculate varying alpha values between 0.3 and 1.0 based on absolute y3 values
alphas = 0.3 + 0.7 * (np.abs(y3) / max(np.abs(y3)))

# Create a scatter plot with varying sizes, colors, and alphas
scatter = ax2.scatter(x, y3, s=sizes, c=colors, cmap='viridis',
                     alpha=alphas)

# Add title and labels to second subplot
ax2.set_title("Scatter Plot with Varying Alpha Based on Y-Value")
ax2.set_xlabel("x")
ax2.set_ylabel("sin(x)cos(x)")
ax2.grid(True, linestyle='--', alpha=0.5)

# Add a colorbar to the second subplot
cbar = plt.colorbar(scatter, ax=ax2)
cbar.set_label('Value of sin(x)cos(x)')

# Adjust layout and show the plot
plt.tight_layout()
plt.show()
```

## Compreendendo o Código e a Saída

Após executar o código, você deve ver uma figura com dois subplots lado a lado:

1. **Primeiro Subplot (Alfa Uniforme)**: Mostra três funções trigonométricas plotadas com o mesmo valor alfa (0.7).

2. **Segundo Subplot (Alfa Variável)**: Mostra um gráfico de dispersão onde:
   - A coordenada x é o valor de entrada
   - A coordenada y é sin(x)cos(x)
   - O tamanho de cada ponto varia com base no valor y absoluto
   - A cor de cada ponto varia com base no valor y
   - O alfa (transparência) de cada ponto varia com base no valor y absoluto

Vamos analisar as partes principais do código:

1. `fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))` - Cria uma figura com dois subplots lado a lado.

2. Para o primeiro subplot:
   - `ax1.plot(..., alpha=0.7)` - Usa um valor alfa uniforme para todas as três linhas.

3. Para o segundo subplot:
   - `alphas = 0.3 + 0.7 * (np.abs(y3) / max(np.abs(y3)))` - Calcula valores alfa variáveis entre 0.3 e 1.0.
   - `ax2.scatter(..., alpha=alphas)` - Usa valores alfa variáveis para os pontos de dispersão.

Esta combinação de técnicas demonstra como os valores alfa podem ser usados de várias maneiras para aprimorar as visualizações:

- **Alfa uniforme** ajuda quando você precisa mostrar múltiplos elementos sobrepostos com igual importância.

- **Alfa variável** ajuda quando você deseja enfatizar certos pontos de dados com base em seus valores.

Ao dominar essas técnicas, você pode criar visualizações de dados mais eficazes e visualmente atraentes.
