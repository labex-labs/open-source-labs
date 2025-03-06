# Einrichten der Bibliotheken und Erstellen von Beispieldaten

In diesem ersten Schritt werden wir die erforderlichen Bibliotheken importieren und Beispieldaten für unser Finanzdiagramm erstellen. Wir müssen sowohl Matplotlib für die Visualisierung als auch NumPy für die Datenerzeugung importieren.

Geben Sie in der ersten Zelle Ihres Notebooks den folgenden Code ein und führen Sie ihn aus, um die benötigten Bibliotheken zu importieren:

```python
# Import necessary libraries
import matplotlib.pyplot as plt
import numpy as np

# Display plots inline in the notebook
%matplotlib inline

print("Libraries imported successfully!")
```

Nachdem Sie den Code ausgeführt haben (drücken Sie Shift+Enter), sollten Sie die folgende Ausgabe sehen:

```
Libraries imported successfully!
```

![libraries-imported](../assets/screenshot-20250306-BN9E08ez@2x.png)

Jetzt erstellen wir einige Beispieldaten für die Finanzvisualisierung. Finanzdaten repräsentieren oft Werte über die Zeit, daher erstellen wir einen einfachen Datensatz, der möglicherweise den täglichen Umsatz über einen bestimmten Zeitraum darstellt.

Fügen Sie in einer neuen Zelle den folgenden Code hinzu und führen Sie ihn aus:

```python
# Set a random seed for reproducibility
np.random.seed(42)

# Generate financial data: 30 days of revenue data
days = np.arange(1, 31)
daily_revenue = np.random.uniform(low=1000, high=5000, size=30)

print("Sample of daily revenue data (first 5 days):")
for i in range(5):
    print(f"Day {days[i]}: ${daily_revenue[i]:.2f}")
```

Nachdem Sie diesen Code ausgeführt haben, werden Sie die ersten 5 Tage unserer Beispielumsatzdaten sehen:

```
Sample of daily revenue data (first 5 days):
Day 1: $3745.40
Day 2: $3992.60
Day 3: $2827.45
Day 4: $4137.54
Day 5: $1579.63
```

Dieser Beispieldatensatz repräsentiert tägliche Umsatzwerte zwischen $1.000 und $5.000 über einen Zeitraum von 30 Tagen. Wir werden diese Daten im nächsten Schritt verwenden, um unser Diagramm zu erstellen.
