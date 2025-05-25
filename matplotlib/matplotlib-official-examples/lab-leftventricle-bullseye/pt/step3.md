# Criando um Gráfico de Dispersão (Scatter Plot)

Criaremos um gráfico de dispersão com valores do eixo X variando de 0 a 5 e os correspondentes valores do eixo Y. Usaremos a função `scatter` fornecida pelo módulo `pyplot` para criar o gráfico de dispersão.

```python
# Criando valores do eixo X
x = np.arange(0, 5, 0.1)

# Criando valores do eixo Y
y = np.sin(x)

# Criando um gráfico de dispersão
plt.scatter(x, y)

# Adicionando título e rótulos ao gráfico
plt.title('Scatter Plot')
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')

# Exibindo o gráfico
plt.show()
```
