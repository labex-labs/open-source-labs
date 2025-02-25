# Text-Wasserzeichen hinzufügen

Um ein Text-Wasserzeichen hinzuzufügen, können wir die `text()`-Methode des `Figure`-Objekts verwenden. Wir müssen die Position, den Text und andere Eigenschaften wie Schriftgröße, Farbe und Transparenz angeben.

```python
ax.text(0.5, 0.5, 'created with matplotlib', transform=ax.transAxes,
        fontsize=40, color='gray', alpha=0.5,
        ha='center', va='center', rotation=30)
```
