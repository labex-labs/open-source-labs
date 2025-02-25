# Fügen einer Legende zum Plot hinzu

Wir werden nun einer Legende zum Plot hinzufügen. Es gibt zwei Möglichkeiten, eine Legende in Matplotlib hinzuzufügen. Wir werden beide Methoden in diesem Beispiel verwenden.

```python
# Methode 1: Legende über dem Teilplot platzieren
ax.legend(bbox_to_anchor=(0., 1.02, 1.,.102), loc='lower left',
           ncols=2, mode="expand", borderaxespad=0.)

# Methode 2: Legende rechts vom Teilplot platzieren
ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
```
