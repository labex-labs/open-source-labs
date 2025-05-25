# Criando um Gráfico de Pizza

Também podemos usar o Matplotlib para criar um gráfico de pizza (pie chart). Neste exemplo, criaremos um gráfico de pizza que mostra a porcentagem de pessoas que preferem diferentes tipos de pizza.

```python
import matplotlib.pyplot as plt

# data to plot
sizes = [30, 40, 10, 20]
labels = ["Pepperoni", "Mushroom", "Onion", "Sausage"]

# creating the pie chart
plt.pie(sizes, labels=labels, autopct='%1.1f%%')

# setting the title
plt.title("Simple Pie Chart")

# displaying the plot
plt.show()
```
