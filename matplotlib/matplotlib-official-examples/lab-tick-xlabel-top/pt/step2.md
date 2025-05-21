# Criando um Gráfico Básico com Configurações Padrão

Agora que importamos o Matplotlib, vamos criar um gráfico simples com as configurações padrão para entender como os eixos e os rótulos de marcação são posicionados por padrão.

## Entendendo os Componentes do Matplotlib

No Matplotlib, os gráficos consistem em vários componentes:

- **Figure** (Figura): O contêiner geral para o gráfico
- **Axes** (Eixos): A área onde os dados são plotados com seu próprio sistema de coordenadas
- **Axis** (Eixo): Os objetos semelhantes a linhas numéricas que definem o sistema de coordenadas
- **Ticks** (Marcações): As marcas nos eixos que denotam valores específicos
- **Tick Labels** (Rótulos de Marcação): Os rótulos de texto que indicam o valor em cada marcação

Por padrão, os rótulos de marcação do eixo x aparecem na parte inferior do gráfico.

## Criando um Gráfico Simples

Em uma nova célula no seu notebook, vamos criar um gráfico de linha simples:

```python
# Create a figure and a set of axes
fig, ax = plt.subplots(figsize=(8, 5))

# Generate some data
x = np.arange(0, 10, 1)
y = np.sin(x)

# Plot the data
ax.plot(x, y, marker='o', linestyle='-', color='blue', label='sin(x)')

# Add a title and labels
ax.set_title('A Simple Sine Wave Plot')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis (sin(x))')

# Add a grid and legend
ax.grid(True, linestyle='--', alpha=0.7)
ax.legend()

# Display the plot
plt.show()

print("Notice that the x-axis tick labels are at the bottom of the plot by default.")
```

Ao executar este código, você verá um gráfico de onda senoidal com os rótulos de marcação do eixo x na parte inferior do gráfico, que é a posição padrão no Matplotlib.

Reserve um momento para observar como o gráfico é estruturado e onde os rótulos de marcação estão posicionados. Essa compreensão nos ajudará a apreciar as mudanças que faremos no próximo passo.
