# Das Diagramm anpassen

Jetzt, nachdem wir ein grundlegendes Diagramm erstellt haben, lassen wir uns es anpassen, um es visuell ansprechender zu gestalten. Wir können einen Titel, Achsenbeschriftungen hinzufügen und die Farbe und den Stil der Linie ändern.

```python
# Add title and axis labels
plt.title('Sin Wave')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Change color and style of line
plt.plot(x, y, color='red', linestyle='dashed')
plt.show()
```
