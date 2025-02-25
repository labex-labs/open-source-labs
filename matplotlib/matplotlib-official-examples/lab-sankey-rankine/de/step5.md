# Hinzufügen von Beschriftungen und Formatierung

Wir werden Beschriftungen zu den Patches im Sankey-Diagramm hinzufügen, indem wir das `text`-Attribut jedes Patches verwenden. Wir werden auch den Text formatieren, um fett zu machen und die Schriftgröße zu erhöhen.

```python
diagrams = sankey.finish()
for diagram in diagrams:
    diagram.text.set_fontweight('bold')
    diagram.text.set_fontsize('10')
    for text in diagram.texts:
        text.set_fontsize('10')
```
