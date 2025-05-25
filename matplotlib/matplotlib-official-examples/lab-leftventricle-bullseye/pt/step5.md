# Criando um Gráfico de Pizza (Pie Chart)

Criaremos um gráfico de pizza com cinco fatias representando diferentes pontos de dados. Usaremos a função `pie` fornecida pelo módulo `pyplot` para criar o gráfico de pizza.

```python
# Criando dados para o gráfico de pizza
data = [10, 20, 30, 25, 15]

# Criando rótulos para o gráfico de pizza
labels = ['Data 1', 'Data 2', 'Data 3', 'Data 4', 'Data 5']

# Criando um gráfico de pizza
plt.pie(data, labels=labels)

# Adicionando título ao gráfico
plt.title('Pie Chart')

# Exibindo o gráfico
plt.show()
```
