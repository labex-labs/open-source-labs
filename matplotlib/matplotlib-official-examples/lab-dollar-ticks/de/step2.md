# Erstellen eines einfachen Finanzdiagramms

Jetzt, da unsere Daten bereit sind, erstellen wir ein einfaches Diagramm, um den täglichen Umsatz zu visualisieren. Wir beginnen mit einem einfachen Linien Diagramm, das den Umsatztrend über den 30 - tägigen Zeitraum zeigt.

Fügen Sie in einer neuen Zelle Ihres Notebooks den folgenden Code hinzu und führen Sie ihn aus:

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

Nachdem Sie diesen Code ausgeführt haben, sollten Sie ein Linien Diagramm sehen, das den täglichen Umsatztrend zeigt. Es sollte in etwa so aussehen (die tatsächlichen Werte können aufgrund der Zufallsgenerierung geringfügig variieren):

![Basic Revenue Plot](../assets/screenshot-20250306-ywFsL4VH@2x.png)

Lassen Sie uns analysieren, was wir in diesem Code getan haben:

1. `fig, ax = plt.subplots(figsize=(10, 6))` - Erstellte eine Figur und Achsen mit einer Größe von 10×6 Zoll
2. `ax.plot(days, daily_revenue, ...)` - Plottete unsere Daten mit den Tagen auf der x - Achse und dem Umsatz auf der y - Achse
3. `ax.set_xlabel()`, `ax.set_ylabel()`, `ax.set_title()` - Fügte Beschriftungen und einen Titel zu unserem Diagramm hinzu
4. `ax.grid()` - Fügte ein Gitter hinzu, um die Daten leichter lesbar zu machen
5. `plt.tight_layout()` - Passte die Abstände an, um sicherzustellen, dass alles gut passt
6. `plt.show()` - Zeigte das Diagramm an

Beachten Sie, dass die y - Achse derzeit einfache Zahlen ohne Dollarzeichen anzeigt. Im nächsten Schritt werden wir unser Diagramm so ändern, dass es eine korrekte Währungsformatierung auf der y - Achse anzeigt.
