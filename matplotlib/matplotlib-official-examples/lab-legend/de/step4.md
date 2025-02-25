# Hinzufügen der Legende

Um der Legende zu unserem Diagramm hinzuzufügen, verwenden wir die `legend`-Funktion von Matplotlib. Wir übergeben das `loc`-Parameter, um den Standort der Legende anzugeben, und den `shadow`-Parameter, um einem Schatteneffekt zur Legende hinzuzufügen. Wir verwenden auch den `fontsize`-Parameter, um die Schriftgröße der Legende festzulegen.

```python
legend = ax.legend(loc='upper center', shadow=True, fontsize='x-large')
```
