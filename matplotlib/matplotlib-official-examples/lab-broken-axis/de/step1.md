# Vorbereitung der Umgebung und Erstellung von Daten

In diesem ersten Schritt richten wir unsere Arbeitsumgebung ein, indem wir die erforderlichen Bibliotheken importieren und Stichprobedaten für unsere Visualisierung erstellen. Wir werden uns darauf konzentrieren, Daten zu generieren, die einige Ausreißer enthalten, um den Nutzen eines Diagramms mit unterbrochener Achse zu demonstrieren.

## Importieren der erforderlichen Bibliotheken

Beginnen wir damit, die Bibliotheken zu importieren, die wir für dieses Tutorial benötigen. Wir werden Matplotlib zur Erstellung unserer Visualisierungen und NumPy zur Generierung und Manipulation von numerischen Daten verwenden.

Erstellen Sie eine neue Zelle in Ihrem Jupyter Notebook und geben Sie den folgenden Code ein:

```python
import matplotlib.pyplot as plt
import numpy as np

print(f"NumPy version: {np.__version__}")
```

Wenn Sie diese Zelle ausführen, sollten Sie eine Ausgabe ähnlich der folgenden sehen:

```
NumPy version: 2.0.0
```

![numpy-version](../assets/screenshot-20250306-Um0MaTKw@2x.png)

Die genauen Versionsnummern können je nach Ihrer Umgebung variieren, aber dies bestätigt, dass die Bibliotheken ordnungsgemäß installiert und einsatzbereit sind.

## Generieren von Stichprobedaten mit Ausreißern

Jetzt erstellen wir einen Stichprobedatensatz, der einige Ausreißer enthält. Wir werden Zufallszahlen generieren und dann absichtlich größere Werte an bestimmte Positionen hinzufügen, um unsere Ausreißer zu erstellen.

Erstellen Sie eine neue Zelle und fügen Sie den folgenden Code hinzu:

```python
# Set random seed for reproducibility
np.random.seed(19680801)

# Generate 30 random points with values between 0 and 0.2
pts = np.random.rand(30) * 0.2

# Add 0.8 to two specific points to create outliers
pts[[3, 14]] += 0.8

# Display the first few data points to understand our dataset
print("First 10 data points:")
print(pts[:10])
print("\nData points containing outliers:")
print(pts[[3, 14]])
```

Wenn Sie diese Zelle ausführen, sollten Sie eine Ausgabe ähnlich der folgenden sehen:

```
First 10 data points:
[0.01182225 0.11765474 0.07404329 0.91088185 0.10502995 0.11190702
 0.14047499 0.01060192 0.15226977 0.06145634]

Data points containing outliers:
[0.91088185 0.97360754]
```

In dieser Ausgabe können Sie deutlich sehen, dass die Werte an den Indizes 3 und 14 viel größer sind als die anderen Werte. Dies sind unsere Ausreißer. Die meisten unserer Datenpunkte liegen unter 0,2, aber diese beiden Ausreißer liegen über 0,9, was in unserem Datensatz eine erhebliche Diskrepanz schafft.

Diese Art der Datenverteilung ist perfekt, um den Nutzen eines Diagramms mit unterbrochener Achse zu demonstrieren. Im nächsten Schritt werden wir die Diagrammstruktur erstellen und sie so konfigurieren, dass sowohl die Hauptdaten als auch die Ausreißer richtig angezeigt werden.
