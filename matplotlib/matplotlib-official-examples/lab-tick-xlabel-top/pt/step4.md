# Personalizando o Gráfico Ainda Mais

Agora que movemos os rótulos de marcação do eixo x para o topo, vamos personalizar ainda mais nosso gráfico para torná-lo mais visualmente atraente e informativo.

## Técnicas Avançadas de Personalização de Gráficos

O Matplotlib oferece inúmeras opções para personalizar gráficos. Vamos explorar algumas dessas opções:

```python
# Create a new figure and a set of axes
fig, ax = plt.subplots(figsize=(10, 6))

# Generate some data with more points for a smoother curve
x = np.linspace(0, 2*np.pi, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Plot multiple datasets
ax.plot(x, y1, linewidth=2, color='blue', label='sin(x)')
ax.plot(x, y2, linewidth=2, color='red', label='cos(x)')

# Fill the area between curves
ax.fill_between(x, y1, y2, where=(y1 > y2), alpha=0.3, color='green', interpolate=True)
ax.fill_between(x, y1, y2, where=(y1 <= y2), alpha=0.3, color='purple', interpolate=True)

# Move the x-axis tick labels to the top
ax.tick_params(
    axis='x',
    top=True,
    labeltop=True,
    bottom=False,
    labelbottom=False
)

# Customize tick labels
ax.set_xticks(np.arange(0, 2*np.pi + 0.1, np.pi/2))
ax.set_xticklabels(['0', 'π/2', 'π', '3π/2', '2π'])

# Add title and labels with custom styles
ax.set_title('Sine and Cosine Functions with Customized X-Axis Labels at the Top',
             fontsize=14, fontweight='bold', pad=20)
ax.set_xlabel('Angle (radians)', fontsize=12)
ax.set_ylabel('Function Value', fontsize=12)

# Add a grid and customize its appearance
ax.grid(True, linestyle='--', alpha=0.7, which='both')

# Customize the axis limits
ax.set_ylim(-1.2, 1.2)

# Add a legend with custom location and style
ax.legend(loc='upper right', fontsize=12, framealpha=0.8)

# Add annotations to highlight important points
ax.annotate('Maximum', xy=(np.pi/2, 1), xytext=(np.pi/2, 1.1),
            arrowprops=dict(facecolor='black', shrink=0.05, width=1.5),
            fontsize=10, ha='center')

# Display the plot
plt.tight_layout()  # Adjust spacing for better appearance
plt.show()

print("We have created a fully customized plot with x-axis tick labels at the top!")
```

Ao executar este código, você verá um gráfico muito mais elaborado e com aparência profissional, com:

- Duas curvas (seno e cosseno)
- Regiões coloridas entre as curvas
- Rótulos de marcação personalizados (usando a notação π)
- Anotações apontando para recursos importantes
- Melhor espaçamento e estilo

Observe como mantivemos os rótulos de marcação do eixo x no topo usando o método `tick_params()`, mas aprimoramos o gráfico com personalizações adicionais.

## Entendendo as Personalizações

Vamos detalhar algumas das principais personalizações que adicionamos:

1. `fill_between()`: Cria regiões coloridas entre as curvas seno e cosseno
2. `set_xticks()` e `set_xticklabels()`: Personalizam as posições e os rótulos das marcações
3. `tight_layout()`: Ajusta automaticamente o espaçamento do gráfico para uma melhor aparência
4. `annotate()`: Adiciona texto com uma seta apontando para um ponto específico
5. Fontes, cores e estilos personalizados para vários elementos

Essas personalizações demonstram como você pode criar gráficos visualmente atraentes e informativos, mantendo os rótulos de marcação do eixo x no topo.
