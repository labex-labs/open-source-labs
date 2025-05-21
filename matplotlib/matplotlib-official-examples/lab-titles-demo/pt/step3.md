# Posicionamento Vertical Personalizado do Título

Às vezes, você pode querer ajustar a posição vertical do seu título. Nesta etapa, você aprenderá como controlar manualmente a posição vertical (eixo y) dos títulos do seu gráfico.

## Entendendo a Posição Y nos Títulos

A posição vertical de um título pode ser ajustada usando o parâmetro `y` na função `title()`. O parâmetro `y` aceita valores em coordenadas normalizadas, onde:

- `y=1.0` (padrão) coloca o título no topo do gráfico
- `y>1.0` coloca o título acima do topo do gráfico
- `y<1.0` coloca o título abaixo do topo do gráfico, movendo-o mais perto do conteúdo do gráfico

## Criando um Gráfico com Posição Y de Título Personalizada

Vamos criar um gráfico com o título posicionado mais alto do que o padrão. Em uma nova célula, insira o seguinte código:

```python
plt.figure(figsize=(8, 5))
plt.plot(range(10))
plt.grid(True)
plt.title('Higher Title Position', y=1.1)  # Position the title higher
plt.show()
```

Execute a célula. Observe como o título agora aparece ligeiramente mais alto acima do gráfico em comparação com a posição padrão.

Agora, vamos criar um gráfico com o título posicionado mais baixo do que o padrão:

```python
plt.figure(figsize=(8, 5))
plt.plot(range(10))
plt.grid(True)
plt.title('Lower Title Position', y=0.9)  # Position the title lower
plt.show()
```

Execute a célula. O título agora deve aparecer mais próximo do conteúdo do gráfico.

## Comparando Diferentes Posições Y

Vamos criar vários gráficos lado a lado para comparar diferentes posições verticais do título:

```python
# Create a figure with 3 subplots arranged horizontally
fig, axes = plt.subplots(1, 3, figsize=(15, 4))

# Plot 1: Default Y-position
axes[0].plot(range(10))
axes[0].grid(True)
axes[0].set_title('Default Position (y=1.0)')

# Plot 2: Higher Y-position
axes[1].plot(range(10))
axes[1].grid(True)
axes[1].set_title('Higher Position', y=1.15)

# Plot 3: Lower Y-position
axes[2].plot(range(10))
axes[2].grid(True)
axes[2].set_title('Lower Position', y=0.85)

plt.tight_layout()  # Adjust spacing between subplots
plt.show()
```

Execute a célula para ver todas as três posições verticais lado a lado. Essa comparação ajuda você a entender como o parâmetro `y` afeta a posição vertical do título.

## Combinando Posicionamento Horizontal e Vertical

Você pode combinar o parâmetro `loc` (para alinhamento horizontal) com o parâmetro `y` (para posição vertical) para colocar seu título exatamente onde você deseja:

```python
plt.figure(figsize=(8, 5))
plt.plot(range(10))
plt.grid(True)
plt.title('Custom Positioned Title', loc='right', y=1.1)  # Right-aligned and higher
plt.show()
```

Execute a célula. O título agora deve aparecer alinhado com a borda direita do gráfico e posicionado mais alto do que o padrão.
