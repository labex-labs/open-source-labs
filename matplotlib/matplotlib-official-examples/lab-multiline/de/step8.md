# Anpassen der X-Achsenbeschriftungen

Um die X-Achsenbeschriftungen anzupassen, können wir die `set_xticks`-Funktion verwenden. Wir können die Positionen und die Beschriftungen der Striche angeben.

```python
ax1.set_xticks([0.2, 0.4, 0.6, 0.8, 1.],
               labels=["Jan\n2009", "Feb\n2009", "Mar\n2009", "Apr\n2009",
                       "May\n2009"])
```
