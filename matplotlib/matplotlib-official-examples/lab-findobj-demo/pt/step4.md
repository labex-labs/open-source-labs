# Personalizando o Gráfico

O Matplotlib oferece uma ampla gama de opções de personalização para gráficos. Aqui está um exemplo de código que personaliza nosso gráfico de linhas simples:

```python
import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Create a plot
plt.plot(x, y, color='red', linewidth=2, linestyle='--', marker='o', markersize=8, markerfacecolor='yellow')

# Add labels and title
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.title('Gráfico Personalizado')

# Display the plot
plt.show()
```

Neste código, usamos vários parâmetros do método `plot()` para personalizar o gráfico. Mudamos a cor da linha para vermelho, a espessura da linha (linewidth) para 2, o estilo da linha (linestyle) para tracejado (`--`), o marcador para um círculo (`o`), o tamanho do marcador (markersize) para 8 e a cor de preenchimento do marcador (markerfacecolor) para amarelo.
