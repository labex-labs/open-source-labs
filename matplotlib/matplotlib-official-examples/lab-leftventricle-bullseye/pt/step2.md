# Criando um Gráfico de Linhas Simples

Criaremos um gráfico de linhas simples com valores do eixo X variando de 0 a 5 e os correspondentes valores do eixo Y. Usaremos a função `plot` fornecida pelo módulo `pyplot` para criar o gráfico de linhas.

```python
# Criando valores do eixo X
x = np.arange(0, 5, 0.1)

# Criando valores do eixo Y
y = np.sin(x)

# Criando um gráfico de linhas
plt.plot(x, y)

# Adicionando título e rótulos ao gráfico
plt.title('Simple Line Plot')
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')

# Exibindo o gráfico
plt.show()
```
