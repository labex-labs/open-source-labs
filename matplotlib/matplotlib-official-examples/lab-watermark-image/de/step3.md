# Erstellen eines einfachen Diagramms mit Zufallsdaten

Bevor wir unser Bild als Überlagerung hinzufügen, müssen wir ein Diagramm erstellen, das als Grundlage für unsere Visualisierung dient. Erstellen wir ein einfaches Balkendiagramm mit Zufallsdaten.

1. Erstellen Sie eine neue Zelle in Ihrem Notebook und geben Sie den folgenden Code ein:

```python
# Create a figure and axes for our plot
fig, ax = plt.subplots(figsize=(10, 6))

# Set a random seed for reproducibility
np.random.seed(19680801)

# Generate random data
x = np.arange(30)  # x-axis values (0 to 29)
y = x + np.random.randn(30)  # y-axis values (x plus random noise)

# Create a bar chart
bars = ax.bar(x, y, color='#6bbc6b')  # Green bars

# Add grid lines
ax.grid(linestyle='--', alpha=0.7)

# Add labels and title
ax.set_xlabel('X-axis Label')
ax.set_ylabel('Y-axis Label')
ax.set_title('Bar Chart with Random Data')

# Display the plot
plt.tight_layout()
plt.show()
```

Dieser Code macht Folgendes:

- Erstellt eine Abbildung und Achsen mit einer bestimmten Größe mithilfe von `plt.subplots()`.
- Setzt einen Zufallssaatwert, um sicherzustellen, dass wir jedes Mal die gleichen Zufallswerte erhalten, wenn wir den Code ausführen.
- Generiert 30 x-Werte (von 0 bis 29) und entsprechende y-Werte (x plus Zufallsrauschen).
- Erstellt ein Balkendiagramm mit grünen Balken mithilfe von `ax.bar()`.
- Fügt Gitterlinien zum Diagramm mit `ax.grid()` hinzu.
- Fügt Beschriftungen für die x-Achse, y-Achse und einen Titel für das Diagramm hinzu.
- Nutzt `plt.tight_layout()`, um den Abstand für ein besseres Erscheinungsbild anzupassen.
- Zeigt das Diagramm mit `plt.show()` an.

2. Führen Sie die Zelle aus, indem Sie Shift+Enter drücken.

Die Ausgabe sollte ein Balkendiagramm mit grünen Balken anzeigen, die die Zufallsdaten repräsentieren. Die x-Achse zeigt ganze Zahlen von 0 bis 29, und die y-Achse zeigt die entsprechenden Werte mit hinzugefügtem Zufallsrauschen.

Dieses Diagramm wird die Grundlage sein, auf der wir in einem nächsten Schritt unser Bild überlagern werden. Beachten Sie, wie wir das Abbildungsobjekt in der Variablen `fig` und das Achsenobjekt in der Variablen `ax` gespeichert haben. Wir werden diese Variablen benötigen, um unser Bild als Überlagerung hinzuzufügen.
