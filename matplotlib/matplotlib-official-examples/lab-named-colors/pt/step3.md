# Criando um Gráfico Simples

Agora que importamos o Matplotlib, podemos usá-lo para criar um gráfico simples. Neste exemplo, criaremos um gráfico de linha que mostra a relação entre os valores de x e y.

```python
import matplotlib.pyplot as plt

# x-axis values
x = [1, 2, 3, 4, 5]

# y-axis values
y = [2, 4, 6, 8, 10]

# plotting the line
plt.plot(x, y)

# setting the title
plt.title("Simple Line Plot")

# setting the x-axis label
plt.xlabel("X-axis")

# setting the y-axis label
plt.ylabel("Y-axis")

# displaying the plot
plt.show()
```
