# Criando um Gráfico de Barras

Também podemos usar o Matplotlib para criar um gráfico de barras (bar plot). Neste exemplo, criaremos um gráfico de barras que mostra o número de maçãs, bananas e laranjas vendidas.

```python
import matplotlib.pyplot as plt

# data to plot
apples = 10
bananas = 15
oranges = 5

# creating the bar plot
plt.bar(["Apples", "Bananas", "Oranges"], [apples, bananas, oranges])

# setting the title
plt.title("Simple Bar Plot")

# setting the x-axis label
plt.xlabel("Fruits")

# setting the y-axis label
plt.ylabel("Quantity")

# displaying the plot
plt.show()
```
