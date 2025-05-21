# Criando um Gráfico de Barras com Valores Alfa Variáveis

Neste passo, usaremos o formato de tupla `(matplotlib_color, alpha)` para atribuir diferentes níveis de transparência a cada barra com base em seu valor de dados.

## Adicionando uma Nova Célula

Adicione uma nova célula ao seu Jupyter Notebook clicando no botão "+" na barra de ferramentas ou pressionando "Esc" seguido de "b" no modo de comando.

## Criando o Gráfico de Barras com Valores Alfa Variáveis

Insira e execute o seguinte código na nova célula:

```python
import matplotlib.pyplot as plt
import numpy as np

# Set a random seed for reproducibility
np.random.seed(19680801)

# Create a figure and an axes
fig, ax = plt.subplots(figsize=(10, 6))

# Generate data (using the same data as in Step 2 for comparison)
x_values = list(range(20))  # 0 to 19
y_values = np.random.randn(20)  # 20 random values from standard normal distribution

# Determine bar colors based on y-values (green for positive, red for negative)
facecolors = ['green' if y > 0 else 'red' for y in y_values]
edgecolors = facecolors  # Same color for edges

# Calculate alpha values based on the absolute y-values
# Normalize y values to get alpha values between 0.2 and 1.0
abs_y = [abs(y) for y in y_values]
max_abs_y = max(abs_y)
face_alphas = [0.2 + 0.8 * (val / max_abs_y) for val in abs_y]

# Create color-alpha tuples for each bar
colors_with_alphas = list(zip(facecolors, face_alphas))

# Create the bar chart with varying alpha values
ax.bar(x_values, y_values, color=colors_with_alphas, edgecolor=edgecolors)

# Add a title and labels
ax.set_title("Bar Chart with Varying Alpha Values Based on Bar Height")
ax.set_xlabel("X Values")
ax.set_ylabel("Y Values")

# Add a grid for better readability
ax.grid(True, linestyle='--', alpha=0.7)

# Show the plot
plt.show()
```

## Compreendendo o Código e a Saída

Após executar o código, você deve ver um gráfico de barras com 20 barras. Cada barra tem um nível de transparência proporcional ao seu valor y absoluto - barras mais altas são mais opacas, barras mais curtas são mais transparentes.

Vamos detalhar as partes principais do código:

1. `abs_y = [abs(y) for y in y_values]` - Isso cria uma lista dos valores absolutos de todos os valores y.

2. `max_abs_y = max(abs_y)` - Encontra o valor absoluto máximo para normalizar os dados.

3. `face_alphas = [0.2 + 0.8 * (val / max_abs_y) for val in abs_y]` - Calcula os valores alfa entre 0.2 e 1.0 com base nos valores y absolutos normalizados.

4. `colors_with_alphas = list(zip(facecolors, face_alphas))` - Cria uma lista de tuplas (cor, alfa) emparelhando cada cor com seu valor alfa correspondente.

5. `ax.bar(..., color=colors_with_alphas, ...)` - Usa as tuplas (cor, alfa) para definir diferentes valores alfa para cada barra.

Esta abordagem de usar níveis de transparência variáveis é eficaz para:

- Enfatizar pontos de dados mais significativos
- Desvalorizar pontos de dados menos significativos
- Criar uma hierarquia visual com base nos valores dos dados
- Adicionar uma dimensão adicional de informação à sua visualização

Você pode ver claramente como os valores alfa variáveis criam um efeito visual onde a magnitude de um ponto de dados é enfatizada tanto pela altura da barra quanto por sua opacidade.
