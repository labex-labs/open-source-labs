# Criando um Gráfico de Barras (Bar Plot)

Criaremos um gráfico de barras com valores do eixo X variando de 0 a 5 e os correspondentes valores do eixo Y. Usaremos a função `bar` fornecida pelo módulo `pyplot` para criar o gráfico de barras.

```python
# Criando valores do eixo X
x = np.arange(0, 5, 0.1)

# Criando valores do eixo Y
y = np.sin(x)

# Criando um gráfico de barras
plt.bar(x, y)

# Adicionando título e rótulos ao gráfico
plt.title('Bar Plot')
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')

# Exibindo o gráfico
plt.show()
```
