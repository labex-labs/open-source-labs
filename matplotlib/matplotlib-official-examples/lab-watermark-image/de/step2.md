# Laden und Untersuchen des Bildes

Nachdem wir unsere Bibliotheken importiert haben, müssen wir das Bild laden, das wir auf unserem Diagramm überlagern möchten. Matplotlib bietet einige Beispielbilder, die wir zum Üben verwenden können.

1. Erstellen Sie eine neue Zelle in Ihrem Notebook und geben Sie den folgenden Code ein:

```python
# Load the sample image
with cbook.get_sample_data('logo2.png') as file:
    im = image.imread(file)

# Display information about the image
print(f"Image shape: {im.shape}")
print(f"Image data type: {im.dtype}")

# Display the image
plt.figure(figsize=(4, 4))
plt.imshow(im)
plt.axis('off')  # Hide axis
plt.title('Matplotlib Logo')
plt.show()
```

Dieser Code macht Folgendes:

- Nutzt `cbook.get_sample_data()`, um ein Beispielbild namens 'logo2.png' aus der Beispiel-Datensammlung von Matplotlib zu laden.
- Nutzt `image.imread()`, um die Bilddatei in ein NumPy-Array einzulesen.
- Gibt Informationen über die Bilddimensionen und den Datentyp aus.
- Erstellt eine Abbildung und zeigt das Bild mit `plt.imshow()` an.
- Blendet die Achsenmarkierungen und -beschriftungen mit `plt.axis('off')` aus.
- Fügt der Abbildung einen Titel hinzu.
- Zeigt die Abbildung mit `plt.show()` an.

2. Führen Sie die Zelle aus, indem Sie Shift+Enter drücken.

Die Ausgabe sollte Informationen über das Bild anzeigen und das Matplotlib-Logo zeigen. Die Bildform gibt die Dimensionen des Bildes an (Höhe, Breite, Farbkanäle), und der Datentyp sagt uns, wie die Bilddaten gespeichert sind.

![image-info](../assets/screenshot-20250306-cqkw4mpg@2x.png)

Dieser Schritt ist wichtig, da er uns hilft, das Bild zu verstehen, das wir als Überlagerung verwenden werden. Wir können sein Aussehen und seine Dimensionen sehen, was nützlich sein wird, wenn wir entscheiden, wie wir es auf unserem Diagramm positionieren möchten.
