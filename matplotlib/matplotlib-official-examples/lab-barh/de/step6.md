# Anpassen des Diagramms

Um das Diagramm informativer zu gestalten, können wir es anpassen, indem wir Beschriftungen, einen Titel hinzufügen und die y-Achse umkehren.

```python
ax.set_yticks(y_pos, labels=people)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel('Performance')
ax.set_title('How fast do you want to go today?')
```
