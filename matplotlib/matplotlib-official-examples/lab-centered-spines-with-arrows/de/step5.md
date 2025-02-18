# Zeichnen von Pfeilen am Ende der Achsenlinien (Spines)

Um die Richtung der Achsen anzuzeigen, können Sie Pfeile am Ende der Achsenlinien (Spines) zeichnen.

```python
ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)
```
