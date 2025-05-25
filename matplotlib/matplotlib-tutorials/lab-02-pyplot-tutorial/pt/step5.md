# Personalizando Propriedades da Linha

Matplotlib permite personalizar várias propriedades da linha, como espessura (linewidth), estilo de traço (dash style) e cor. Vamos demonstrar algumas maneiras de definir as propriedades da linha:

```python
x = np.arange(0, 5, 0.1)
line, = plt.plot(x, np.sin(x), '-')

# Using the Line2D instance's setter method
line.set_linewidth(2.0)  # Set the linewidth property of the line to 2.0

# Using the pyplot.setp function
plt.setp(line, color='r', linewidth=2.0)  # Set the color and linewidth properties using the setp function

plt.show()
```

Explicação:

- Criamos um array `x` e calculamos os valores de y correspondentes usando a função `np.sin`.
- A função `plot` é chamada para criar um gráfico de linhas.
- Usamos o método `set` da instância `Line2D` para definir a propriedade de espessura (linewidth) da linha para 2.0.
- Alternativamente, podemos usar a função `setp` para definir múltiplas propriedades da linha, como cor e espessura (linewidth), usando argumentos de palavra-chave.
