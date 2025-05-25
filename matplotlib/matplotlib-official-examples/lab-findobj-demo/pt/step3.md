# Criando um Gráfico Simples

O gráfico mais básico em Matplotlib é um gráfico de linhas. Você pode criar um gráfico de linhas usando o método `plot()`. Aqui está um exemplo de código que cria um gráfico de linhas simples:

```python
import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Create a plot
plt.plot(x, y)

# Add labels and title
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.title('Gráfico Simples')

# Display the plot
plt.show()
```

Neste código, primeiro definimos nossos pontos de dados como duas listas `x` e `y`. Em seguida, criamos um gráfico usando o método `plot()` e passamos nossos pontos de dados. Depois, adicionamos rótulos aos eixos X e Y e um título ao gráfico usando os métodos `xlabel()`, `ylabel()` e `title()`. Finalmente, exibimos o gráfico usando o método `show()`.
