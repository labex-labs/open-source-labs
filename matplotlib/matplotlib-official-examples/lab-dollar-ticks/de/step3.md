# Formatieren der Y-Achsenbeschriftungen mit Dollarzeichen

Jetzt, da wir unser einfaches Diagramm haben, formatieren wir die Beschriftungen der Y-Achse, um Dollarzeichen anzuzeigen. Dies macht unsere Finanzdaten lesbarer und gibt ihnen ein professionelles Aussehen.

Um die Markierungsbeschriftungen auf der Y-Achse zu formatieren, verwenden wir das `ticker`-Modul von Matplotlib, das verschiedene Formatierungsoptionen bietet. Insbesondere verwenden wir die `StrMethodFormatter`-Klasse, um einen benutzerdefinierten Formatter für unsere Y-Achse zu erstellen.

Fügen Sie in einer neuen Zelle Ihres Notebooks den folgenden Code hinzu und führen Sie ihn aus:

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

Nachdem Sie diesen Code ausgeführt haben, sollten Sie ein neues Diagramm sehen, bei dem die Beschriftungen der Y-Achse Dollarzeichen enthalten.

Lassen Sie uns den wichtigsten Teil dieses Codes erklären:

```python
formatter = ticker.StrMethodFormatter('${x:,.2f}')
ax.yaxis.set_major_formatter(formatter)
```

Hier ist, was diese Formatierungszeichenfolge bewirkt:

- `$` - Fügt ein Dollarzeichen am Anfang jeder Beschriftung hinzu
- `{x:,.2f}` - Formatiert die Zahl wie folgt:
  - `,` - Komma als Tausendertrennzeichen (z.B. 1.000 statt 1000)
  - `.2f` - Zwei Dezimalstellen (z.B. $1.234,56)

Dieser Formatter wird auf alle Hauptmarkierungsbeschriftungen der Y-Achse angewendet. Beachten Sie, wie das Diagramm nun deutlich zeigt, dass es sich bei den Werten um Dollar handelt, was es für die Visualisierung von Finanzdaten viel geeigneter macht.
