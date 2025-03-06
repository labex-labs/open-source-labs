# Speichern des Diagramms und Erstellen einer wiederverwendbaren Funktion

In diesem letzten Schritt erstellen wir eine wiederverwendbare Funktion, um Währungsformatierte Diagramme zu generieren und unsere Visualisierung in einer Datei zu speichern. Dieser Ansatz erleichtert es, in Zukunft die gleiche Formatierung auf verschiedene Finanzdatensätze anzuwenden.

Fügen Sie in einer neuen Zelle Ihres Notebooks den folgenden Code hinzu und führen Sie ihn aus:

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

Nachdem Sie diesen Code ausgeführt haben, sollten Sie Folgendes sehen:

1. Ein ähnliches Diagramm wie das, das wir im vorherigen Schritt erstellt haben, aber mit unserer benutzerdefinierten Funktion generiert
2. Eine Meldung, die bestätigt, dass das Diagramm in einer Datei namens `revenue_plot.png` gespeichert wurde

Die Funktion, die wir erstellt haben:

- Nimmt Daten für die X- und Y-Achsen entgegen
- Ermöglicht die Anpassung von Beschriftungen und Titel
- Bietet die Möglichkeit, das Diagramm in einer Datei zu speichern
- Kann Statistiken wie Durchschnitt, Minimum und Maximum anzeigen oder ausblenden
- Gibt die Figure- und Axes-Objekte zurück, falls weitere Anpassungen erforderlich sind

Diese wiederverwendbare Funktion erleichtert es, in Zukunft konsistent formatierte Finanzdiagramme zu erstellen. Sie können einfach diese Funktion mit verschiedenen Datensätzen aufrufen, und sie wird automatisch alle Währungsformatierungen und statistischen Anmerkungen verarbeiten.

Um zu überprüfen, ob unser Diagramm korrekt gespeichert wurde, überprüfen wir, ob die Datei existiert:

```python
import os
if os.path.exists('revenue_plot.png'):
    print("Plot file exists! Size:", os.path.getsize('revenue_plot.png'), "bytes")
else:
    print("Plot file was not saved correctly.")
```

Sie sollten eine Meldung sehen, die bestätigt, dass die Datei existiert und ihre Größe angibt.

Herzlichen Glückwunsch! Sie haben erfolgreich gelernt, wie Sie Diagramme mit Dollarzeichen formatieren und professionell aussehende Finanzvisualisierungen mit Matplotlib erstellen.
