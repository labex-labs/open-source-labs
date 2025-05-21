# Criando um Gráfico de Dispersão com Valores Alfa

Neste passo, aplicaremos nosso conhecimento sobre valores alfa para criar um gráfico de dispersão. Isso demonstrará como a transparência pode ajudar a visualizar a densidade dos dados em gráficos de dispersão com pontos sobrepostos.

## Adicionando uma Nova Célula

Adicione uma nova célula ao seu Jupyter Notebook clicando no botão "+" na barra de ferramentas ou pressionando "Esc" seguido de "b" no modo de comando.

## Criando um Gráfico de Dispersão com Transparência

Insira e execute o seguinte código na nova célula:

```python
import matplotlib.pyplot as plt
import numpy as np

# Set a random seed for reproducibility
np.random.seed(19680801)

# Create a figure and an axes
fig, ax = plt.subplots(figsize=(10, 6))

# Create two clusters of points
cluster1_x = np.random.normal(0.3, 0.15, 500)
cluster1_y = np.random.normal(0.3, 0.15, 500)

cluster2_x = np.random.normal(0.7, 0.15, 500)
cluster2_y = np.random.normal(0.7, 0.15, 500)

# Combine the clusters
x = np.concatenate([cluster1_x, cluster2_x])
y = np.concatenate([cluster1_y, cluster2_y])

# Create a scatter plot with alpha=0.5
scatter = ax.scatter(x, y, s=30, c='blue', alpha=0.5)

# Add a title and labels
ax.set_title("Scatter Plot with Alpha=0.5 Showing Data Density")
ax.set_xlabel("X")
ax.set_ylabel("Y")

# Set axis limits
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)

# Add a grid
ax.grid(True, linestyle='--', alpha=0.7)

# Show the plot
plt.show()
```

## Compreendendo o Código e a Saída

Após executar o código, você deve ver um gráfico de dispersão com dois clusters de pontos. Cada ponto tem um nível de transparência de 0.5, o que permite que você veja onde os pontos se sobrepõem.

Vamos detalhar as partes principais do código:

1. `cluster1_x = np.random.normal(0.3, 0.15, 500)` - Gera 500 coordenadas x aleatórias seguindo uma distribuição normal com média 0.3 e desvio padrão 0.15.

2. `cluster1_y = np.random.normal(0.3, 0.15, 500)` - Gera 500 coordenadas y aleatórias para o primeiro cluster.

3. `cluster2_x` e `cluster2_y` - Semelhantemente, geram coordenadas para o segundo cluster centrado em (0.7, 0.7).

4. `ax.scatter(..., alpha=0.5)` - Cria um gráfico de dispersão com pontos a 50% de opacidade.

Os benefícios de usar alfa em gráficos de dispersão incluem:

1. **Visualização da Densidade**: Áreas onde muitos pontos se sobrepõem aparecem mais escuras, revelando a densidade dos dados.

2. **Redução de Overplotting**: Sem transparência, os pontos sobrepostos se esconderiam completamente uns aos outros.

3. **Reconhecimento de Padrões**: A transparência ajuda a identificar clusters e padrões nos dados.

Observe como as áreas com mais pontos sobrepostos aparecem mais escuras na visualização. Esta é uma maneira poderosa de visualizar a densidade dos dados sem precisar de técnicas adicionais como estimativa de densidade.
