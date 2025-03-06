# Personnaliser davantage le graphique

Maintenant que nous avons déplacé les étiquettes de graduation de l'axe des x en haut, personnalisons davantage notre graphique pour le rendre plus attrayant visuellement et plus informatif.

## Techniques avancées de personnalisation de graphiques

Matplotlib offre de nombreuses options pour personnaliser les graphiques. Explorons quelques-unes de ces options :

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

Lorsque vous exécutez ce code, vous verrez un graphique beaucoup plus élaboré et professionnel avec :

- Deux courbes (sinus et cosinus)
- Des régions colorées entre les courbes
- Des étiquettes de graduation personnalisées (utilisant la notation π)
- Des annotations pointant vers les éléments clés
- Un meilleur espacement et un meilleur style

Remarquez comment nous avons maintenu les étiquettes de graduation de l'axe des x en haut en utilisant la méthode `tick_params()` tout en améliorant le graphique avec des personnalisations supplémentaires.

## Comprendre les personnalisations

Décortiquons quelques-unes des personnalisations clés que nous avons ajoutées :

1. `fill_between()` : Crée des régions colorées entre les courbes de sinus et de cosinus
2. `set_xticks()` et `set_xticklabels()` : Personnalisent les positions et les étiquettes des graduations
3. `tight_layout()` : Ajuste automatiquement l'espacement du graphique pour un meilleur aspect
4. `annotate()` : Ajoute du texte avec une flèche pointant vers un point spécifique
5. Des polices, des couleurs et des styles personnalisés pour divers éléments

Ces personnalisations montrent comment vous pouvez créer des graphiques visuellement attrayants et informatifs tout en gardant les étiquettes de graduation de l'axe des x en haut.
