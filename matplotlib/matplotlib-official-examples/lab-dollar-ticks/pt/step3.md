# Formatando Rótulos do Eixo Y com Sinais de Dólar

Agora que temos nosso gráfico básico, vamos formatar os rótulos do eixo y para exibir sinais de dólar. Isso tornará nossos dados financeiros mais legíveis e profissionalmente apresentados.

Para formatar os rótulos de marcação no eixo y, usaremos o módulo `ticker` do Matplotlib, que fornece várias opções de formatação. Especificamente, usaremos a classe `StrMethodFormatter` para criar um formatador personalizado para nosso eixo y.

Em uma nova célula no seu notebook, adicione e execute o seguinte código:

```python
# Import the necessary module for formatting
import matplotlib.ticker as ticker

# Create a figure and axes
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the daily revenue data
ax.plot(days, daily_revenue, marker='o', linestyle='-', color='blue', linewidth=2, markersize=6)

# Format y-axis with dollar signs
formatter = ticker.StrMethodFormatter('${x:,.2f}')
ax.yaxis.set_major_formatter(formatter)

# Add labels and title
ax.set_xlabel('Day', fontsize=12)
ax.set_ylabel('Revenue ($)', fontsize=12)
ax.set_title('Daily Revenue Over 30 Days', fontsize=14, fontweight='bold')

# Add grid for better readability
ax.grid(True, linestyle='--', alpha=0.7)

# Display the plot
plt.tight_layout()
plt.show()

print("Plot with dollar-formatted y-axis created!")
```

Após executar este código, você deverá ver um novo gráfico com sinais de dólar nos rótulos do eixo y.

Vamos explicar a parte chave deste código:

```python
formatter = ticker.StrMethodFormatter('${x:,.2f}')
ax.yaxis.set_major_formatter(formatter)
```

Aqui está o que esta string de formatação faz:

- `$` - Adiciona um sinal de dólar no início de cada rótulo
- `{x:,.2f}` - Formata o número com:
  - `,` - Vírgula como separador de milhares (por exemplo, 1.000 em vez de 1000)
  - `.2f` - Duas casas decimais (por exemplo, $1.234,56)

Este formatador se aplica a todos os rótulos de marcação principais no eixo y. Observe como o gráfico agora indica claramente que os valores estão em dólares, tornando-o muito mais apropriado para a visualização de dados financeiros.
