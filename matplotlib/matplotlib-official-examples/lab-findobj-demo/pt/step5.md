# Criando Diferentes Tipos de Gráficos

O Matplotlib suporta uma ampla gama de tipos de gráficos, incluindo gráficos de linhas, gráficos de dispersão (scatter plots), gráficos de barras e muito mais. Aqui está um exemplo de código que cria um gráfico de dispersão:

```python
import matplotlib.pyplot as plt
import numpy as np

# Generate some random data
x = np.random.rand(50)
y = np.random.rand(50)
colors = np.random.rand(50)
sizes = 1000 * np.random.rand(50)

# Create a scatter plot
plt.scatter(x, y, c=colors, s=sizes, alpha=0.5)

# Add labels and title
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.title('Gráfico de Dispersão')

# Display the plot
plt.show()
```

Neste código, usamos o método `scatter()` para criar um gráfico de dispersão. Geramos alguns dados aleatórios usando a biblioteca NumPy e os passamos para o método `scatter()`. Também usamos o parâmetro `c` para especificar as cores dos pontos de dados, o parâmetro `s` para especificar os tamanhos dos pontos de dados e o parâmetro `alpha` para especificar a transparência dos pontos de dados.
