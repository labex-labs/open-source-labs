# Grundlagen von Matplotlib und Erstellung eines Notebooks

In diesem ersten Schritt werden wir uns mit Matplotlib vertraut machen und ein neues Jupyter-Notebook für unsere Visualisierungsaufgabe erstellen.

## Was ist Matplotlib?

Matplotlib ist eine umfassende Bibliothek zur Erstellung von statischen, animierten und interaktiven Visualisierungen in Python. Sie bietet eine objektorientierte API (Anwendungs-Programmierschnittstelle) zum Einbetten von Diagrammen in Anwendungen und wird von Wissenschaftlern, Ingenieuren und Datenanalysten häufig für die Datenvisualisierung eingesetzt.

## Erstellen eines neuen Notebooks

Lassen Sie uns in der ersten Zelle Ihres Notebooks die Matplotlib-Bibliothek importieren. Geben Sie den folgenden Code ein und führen Sie die Zelle aus, indem Sie Shift+Enter drücken:

```python
import matplotlib.pyplot as plt
import numpy as np

# Check the Matplotlib version
print(f"NumPy version: {np.__version__}")
```

![libraries-imported](../assets/screenshot-20250306-K6iIFfj1@2x.png)

Wenn Sie diesen Code ausführen, sollten Sie eine Ausgabe ähnlich der folgenden sehen:

```
NumPy version: 2.0.0
```

Die genaue Versionsnummer kann je nach Ihrer Umgebung variieren.

Jetzt haben wir Matplotlib importiert und können es verwenden. `plt` ist ein üblicher Alias für das pyplot-Modul, das eine MATLAB-ähnliche Schnittstelle zur Erstellung von Diagrammen bietet.
