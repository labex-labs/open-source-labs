# Enregistrement du graphique et création d'une fonction réutilisable

Dans cette étape finale, nous allons créer une fonction réutilisable pour générer des graphiques formatés en devise et enregistrer notre visualisation dans un fichier. Cette approche facilite l'application du même formatage à différents ensembles de données financières à l'avenir.

Dans une nouvelle cellule de votre notebook, ajoutez et exécutez le code suivant :

```python
def create_currency_plot(x_data, y_data, title='Financial Data',
                         xlabel='X-Axis', ylabel='Amount ($)',
                         filename=None, show_stats=True):
    """
    Create a plot with currency formatting on the y-axis.

    Parameters:
    -----------
    x_data : array-like
        Data for the x-axis
    y_data : array-like
        Data for the y-axis (currency values)
    title : str
        Title of the plot
    xlabel : str
        Label for the x-axis
    ylabel : str
        Label for the y-axis
    filename : str, optional
        If provided, save the plot to this filename
    show_stats : bool
        Whether to show statistics (average, min, max)

    Returns:
    --------
    fig, ax : tuple
        The figure and axes objects
    """
    # Import the necessary module for formatting
    import matplotlib.ticker as ticker

    # Create a figure and axes
    fig, ax = plt.subplots(figsize=(12, 7))

    # Plot the data
    ax.plot(x_data, y_data, marker='o', linestyle='-', color='blue',
            linewidth=2, markersize=6, label='Data')

    if show_stats:
        # Calculate statistics
        avg_value = np.mean(y_data)
        max_value = np.max(y_data)
        min_value = np.min(y_data)
        max_x = x_data[np.argmax(y_data)]
        min_x = x_data[np.argmin(y_data)]

        # Add a horizontal line for average value
        ax.axhline(y=avg_value, color='r', linestyle='--', alpha=0.7,
                   label=f'Average: ${avg_value:.2f}')

        # Add annotations for max and min values
        ax.annotate(f'Max: ${max_value:.2f}', xy=(max_x, max_value),
                    xytext=(max_x+1, max_value+200),
                    arrowprops=dict(facecolor='black', shrink=0.05, width=1.5))

        ax.annotate(f'Min: ${min_value:.2f}', xy=(min_x, min_value),
                    xytext=(min_x+1, min_value-200),
                    arrowprops=dict(facecolor='black', shrink=0.05, width=1.5))

    # Format y-axis with dollar signs
    formatter = ticker.StrMethodFormatter('${x:,.2f}')
    ax.yaxis.set_major_formatter(formatter)

    # Customize tick parameters
    ax.tick_params(axis='both', which='major', labelsize=10)

    # Add labels and title
    ax.set_xlabel(xlabel, fontsize=12)
    ax.set_ylabel(ylabel, fontsize=12)
    ax.set_title(title, fontsize=14, fontweight='bold')

    # Add grid for better readability
    ax.grid(True, linestyle='--', alpha=0.7)

    # Add legend
    if show_stats:
        ax.legend(loc='best', fontsize=10)

    # Adjust layout
    plt.tight_layout()

    # Save the plot if filename is provided
    if filename:
        plt.savefig(filename, dpi=300, bbox_inches='tight')
        print(f"Plot saved as '{filename}'")

    return fig, ax

# Use our function to create and save a plot
fig, ax = create_currency_plot(
    days,
    daily_revenue,
    title='Monthly Revenue Report',
    xlabel='Day of Month',
    ylabel='Daily Revenue ($)',
    filename='revenue_plot.png'
)

# Display the plot
plt.show()

print("Function created and plot saved successfully!")
```

Après avoir exécuté ce code, vous devriez voir :

1. Un graphique similaire à celui que nous avons créé à l'étape précédente, mais généré à l'aide de notre fonction personnalisée
2. Un message confirmant que le graphique a été enregistré dans un fichier nommé `revenue_plot.png`

La fonction que nous avons créée :

- Prend en compte les données pour les axes x et y
- Permet de personnaliser les étiquettes et le titre
- Offre la possibilité d'enregistrer le graphique dans un fichier
- Peut afficher ou masquer des statistiques telles que la moyenne, le minimum et le maximum
- Renvoie les objets figure et axes pour une personnalisation supplémentaire si nécessaire

Cette fonction réutilisable facilite la création de graphiques financiers formatés de manière cohérente à l'avenir. Vous pouvez simplement appeler cette fonction avec différents ensembles de données, et elle gérera automatiquement tout le formatage monétaire et les annotations statistiques.

Pour vérifier que notre graphique a été enregistré correctement, vérifions si le fichier existe :

```python
import os
if os.path.exists('revenue_plot.png'):
    print("Plot file exists! Size:", os.path.getsize('revenue_plot.png'), "bytes")
else:
    print("Plot file was not saved correctly.")
```

Vous devriez voir un message confirmant que le fichier existe et indiquant sa taille.

Félicitations ! Vous avez appris avec succès à formater des graphiques avec des signes dollars et à créer des visualisations financières de qualité professionnelle à l'aide de Matplotlib.
