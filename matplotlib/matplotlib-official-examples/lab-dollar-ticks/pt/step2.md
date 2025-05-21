# Criando um Gráfico Financeiro Básico

Agora que temos nossos dados prontos, vamos criar um gráfico básico para visualizar a receita diária. Começaremos com um gráfico de linha simples que mostra a tendência da receita ao longo do período de 30 dias.

Em uma nova célula no seu notebook, adicione e execute o seguinte código:

```python
# Create a figure and axes
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the daily revenue data
ax.plot(days, daily_revenue, marker='o', linestyle='-', color='blue', linewidth=2, markersize=6)

# Add labels and title
ax.set_xlabel('Day', fontsize=12)
ax.set_ylabel('Revenue', fontsize=12)
ax.set_title('Daily Revenue Over 30 Days', fontsize=14, fontweight='bold')

# Add grid for better readability
ax.grid(True, linestyle='--', alpha=0.7)

# Display the plot
plt.tight_layout()
plt.show()

print("Basic plot created successfully!")
```

Após executar este código, você deverá ver um gráfico de linha mostrando a tendência da receita diária. Ele deve se parecer com isto (os valores reais podem variar ligeiramente devido à geração aleatória):

![Basic Revenue Plot](../assets/screenshot-20250306-ywFsL4VH@2x.png)

Vamos detalhar o que fizemos neste código:

1. `fig, ax = plt.subplots(figsize=(10, 6))` - Criou uma figura e eixos com um tamanho de 10×6 polegadas
2. `ax.plot(days, daily_revenue, ...)` - Plotou nossos dados com os dias no eixo x e a receita no eixo y
3. `ax.set_xlabel()`, `ax.set_ylabel()`, `ax.set_title()` - Adicionou rótulos e um título ao nosso gráfico
4. `ax.grid()` - Adicionou uma grade para facilitar a leitura dos dados
5. `plt.tight_layout()` - Ajustou o preenchimento para garantir que tudo se encaixe bem
6. `plt.show()` - Exibiu o gráfico

Observe que o eixo y atualmente mostra números simples sem sinais de dólar. No próximo passo, modificaremos nosso gráfico para exibir a formatação de moeda adequada no eixo y.
