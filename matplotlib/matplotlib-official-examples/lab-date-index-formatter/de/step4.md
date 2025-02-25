# Verwenden eines aufrufbaren Objekts als Formatter

Anstatt eine Funktion an `.Axis.set_major_formatter` zu übergeben, können wir jedes andere aufrufbare Objekt verwenden, wie z. B. eine Instanz einer Klasse, die `__call__` implementiert. In diesem Schritt werden wir eine Klasse `MyFormatter` erstellen, die die Striche als Zeiten formatiert.

```python
# Use a callable for formatter
class MyFormatter(Formatter):
    def __init__(self, dates, fmt='%a'):
        self.dates = dates
        self.fmt = fmt

    def __call__(self, x, pos=0):
        """Return the label for time x at position pos."""
        try:
            return self.dates[round(x)].item().strftime(self.fmt)
        except IndexError:
            pass

ax2.xaxis.set_major_formatter(MyFormatter(r.date, '%a'))
```
