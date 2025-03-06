# Grundlegende Diagrammerstellung mit Standardtitelposition

In diesem Schritt erstellen Sie ein einfaches Linien Diagramm und fügen einen zentrierten Titel hinzu, was die Standardposition in Matplotlib ist.

## Erstellen eines Jupyter Notebooks

Nachdem der Start der virtuellen Maschine abgeschlossen ist, klicken Sie in der oberen linken Ecke, um zur Registerkarte **Notebook** zu wechseln und auf Jupyter Notebook zuzugreifen.

![click-notebook](https://file.labex.io/images/click-notebook.png)

Sie müssen möglicherweise einige Sekunden warten, bis Jupyter Notebook fertig geladen hat. Aufgrund der Einschränkungen von Jupyter Notebook kann die Validierung von Vorgängen nicht automatisiert werden.

Wenn Sie während des Labs auf Probleme stoßen, können Sie sich gerne an Labby wenden. Bitte geben Sie nach der Sitzung Feedback ab, damit wir alle Probleme umgehend beheben können.

## Importieren von Matplotlib

Jetzt beginnen wir mit dem Importieren der Matplotlib-Bibliothek. Geben Sie in der ersten Zelle Ihres Notebooks den folgenden Code ein und führen Sie ihn aus, indem Sie Shift+Enter drücken:

```python
import matplotlib.pyplot as plt
```

Dies importiert das pyplot-Modul aus Matplotlib und weist es dem Alias `plt` zu, was eine gängige Konvention ist.

## Erstellen eines einfachen Diagramms

Als Nächstes erstellen wir ein einfaches Linien Diagramm. Geben Sie in einer neuen Zelle den folgenden Code ein und führen Sie ihn aus:

```python
plt.figure(figsize=(8, 5))  # Create a figure with a specific size
plt.plot(range(10))         # Plot numbers from 0 to 9
plt.grid(True)              # Add a grid for better readability
plt.show()                  # Display the plot
```

Sie sollten ein einfaches Linien Diagramm mit Werten von 0 bis 9 in der Ausgabe sehen.

![line-plot](../assets/screenshot-20250306-g5knGobR@2x.png)

## Hinzufügen eines Standard- (zentrierten) Titels

Jetzt fügen wir unserem Diagramm einen Titel hinzu. Die Standardposition für einen Titel ist zentriert entlang der oberen Seite des Diagramms. Geben Sie in einer neuen Zelle den folgenden Code ein:

```python
plt.figure(figsize=(8, 5))
plt.plot(range(10))
plt.grid(True)
plt.title('My First Matplotlib Plot')  # Add a centered title
plt.show()
```

![line-plot-with-title](../assets/screenshot-20250306-XMODABB2@2x.png)

Führen Sie die Zelle aus, und Sie sollten das Diagramm mit einem zentrierten Titel oben sehen.

Die `title()`-Funktion ohne zusätzliche Parameter platziert den Titel in der Mitte, was die Standardposition ist.
