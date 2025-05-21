# Compreendendo os Valores Alfa no Matplotlib

Neste primeiro passo, criaremos um Jupyter Notebook e aprenderemos como configurar uma visualização básica com valores alfa.

## Criando sua Primeira Célula Jupyter Notebook

Nesta célula, importaremos as bibliotecas necessárias e criaremos dois círculos sobrepostos com diferentes valores alfa para demonstrar a transparência.

```python
import matplotlib.pyplot as plt
import numpy as np

# Create a figure and an axes
fig, ax = plt.subplots(figsize=(6, 4))

# Create a circle with alpha=1.0 (completely opaque)
circle1 = plt.Circle((0.5, 0.5), 0.3, color='blue', alpha=1.0, label='Opaque (alpha=1.0)')

# Create a circle with alpha=0.5 (semi-transparent)
circle2 = plt.Circle((0.7, 0.5), 0.3, color='red', alpha=0.5, label='Semi-transparent (alpha=0.5)')

# Add circles to the axes
ax.add_patch(circle1)
ax.add_patch(circle2)

# Set axis limits
ax.set_xlim(0, 1.2)
ax.set_ylim(0, 1)

# Add a title and legend
ax.set_title('Demonstrating Alpha Values in Matplotlib')
ax.legend(loc='upper right')

# Show the plot
plt.show()
```

Depois de inserir este código na célula, execute-o pressionando Shift+Enter ou clicando no botão "Run" na barra de ferramentas.

## Compreendendo a Saída

Você deve ver dois círculos sobrepostos:

- O círculo azul à esquerda é completamente opaco (alpha=1.0)
- O círculo vermelho à direita é semi-transparente (alpha=0.5)

Observe como você pode ver o círculo azul através do vermelho onde eles se sobrepõem. Este é o efeito de definir o valor alfa como 0.5 para o círculo vermelho.

Os valores alfa controlam a transparência nas visualizações e podem ajudar quando:

- Mostrando pontos de dados sobrepostos
- Destacando certos elementos
- Reduzindo a desordem visual em gráficos densos
- Criando visualizações em camadas

Vamos continuar a explorar mais aplicações dos valores alfa no próximo passo.
