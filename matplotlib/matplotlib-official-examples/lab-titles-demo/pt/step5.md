# Posicionamento Global de Títulos com RCParams

Nesta etapa final, você aprenderá como usar os parâmetros de configuração de tempo de execução (RCParams) do Matplotlib para definir padrões globais para o posicionamento de títulos. Isso é útil quando você deseja que todos os gráficos em seu notebook ou script usem um posicionamento de título consistente sem ter que especificá-lo para cada gráfico individualmente.

## Entendendo RCParams no Matplotlib

O comportamento do Matplotlib pode ser personalizado usando uma variável semelhante a um dicionário chamada `rcParams`. Isso permite que você defina padrões globais para várias propriedades, incluindo o posicionamento do título.

## Definindo o Posicionamento Global do Título com rcParams

Vamos definir padrões globais para o posicionamento do título e, em seguida, criar alguns gráficos que usarão automaticamente essas configurações:

```python
# View the current default values
print("Default title y position:", plt.rcParams['axes.titley'])
print("Default title padding:", plt.rcParams['axes.titlepad'])
```

Execute a célula para ver os valores padrão. Agora, vamos modificar essas configurações:

```python
# Set new global defaults for title positioning
plt.rcParams['axes.titley'] = 1.05     # Set title y position higher
plt.rcParams['axes.titlepad'] = 10     # Set padding between title and plot
plt.rcParams['axes.titlelocation'] = 'left'  # Set default alignment to left

# Create a plot that will use the new defaults
plt.figure(figsize=(8, 5))
plt.plot(range(10))
plt.grid(True)
plt.title('This Title Uses Global RCParams Settings')
plt.show()
```

Execute a célula. Observe como o título é posicionado de acordo com as configurações globais que definimos, mesmo que não tenhamos especificado nenhum parâmetro de posicionamento na função `title()`.

## Criando Vários Gráficos com as Mesmas Configurações

Vamos criar vários gráficos que usam todas as nossas configurações globais:

```python
# Create a figure with a 2x2 grid of subplots
fig, axes = plt.subplots(2, 2, figsize=(10, 8))

# Flatten the 2D array of axes for easier iteration
axes = axes.flatten()

# Plot data on each subplot with titles that use global settings
for i, ax in enumerate(axes):
    ax.plot(range(10))
    ax.grid(True)
    ax.set_title(f'Subplot {i+1} Using Global Settings')

plt.tight_layout()
plt.show()
```

Execute a célula. Todos os quatro títulos de subplot devem ser posicionados de acordo com as configurações globais que definimos anteriormente.

## Redefinindo RCParams para os Padrões

Se você quiser redefinir os RCParams para seus valores padrão, você pode usar a função `rcdefaults()`:

```python
# Reset to default settings
plt.rcdefaults()

# Create a plot with default settings
plt.figure(figsize=(8, 5))
plt.plot(range(10))
plt.grid(True)
plt.title('This Title Uses Default Settings Again')
plt.show()
```

Execute a célula. O título agora deve ser posicionado usando as configurações padrão do Matplotlib.

## Mudanças Temporárias nos RCParams

Se você quiser alterar temporariamente os RCParams apenas para uma seção específica do seu código, você pode usar um gerenciador de contexto:

```python
# Create a plot with default settings
plt.figure(figsize=(8, 5))
plt.plot(range(10))
plt.grid(True)
plt.title('Default Settings')
plt.show()

# Temporarily change RCParams for just this section
with plt.rc_context({'axes.titlelocation': 'right', 'axes.titley': 1.1}):
    plt.figure(figsize=(8, 5))
    plt.plot(range(10))
    plt.grid(True)
    plt.title('Temporary Settings Change')
    plt.show()

# Create another plot that will use default settings again
plt.figure(figsize=(8, 5))
plt.plot(range(10))
plt.grid(True)
plt.title('Back to Default Settings')
plt.show()
```

Execute a célula. Você deve ver três gráficos:

1. O primeiro com posicionamento de título padrão
2. O segundo com título alinhado à direita e posicionado mais alto (devido às configurações temporárias)
3. O terceiro com posicionamento de título padrão novamente (pois as configurações temporárias só se aplicaram dentro do gerenciador de contexto)

Essa abordagem permite que você faça alterações temporárias nas configurações globais sem afetar o restante de seus gráficos.
