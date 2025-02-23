# Automatisches Umbrechen von Text

Jetzt wollen wir untersuchen, wie man in Matplotlib Text automatisch umbricht. Ersetzen Sie die Zeile `plt.text()` in Ihrem Code durch Folgendes:

```python
t = ("This is a really long string that I'd rather have wrapped so that it "
     "doesn't go outside of the figure, but if it's long enough it will go "
     "off the top or bottom!")
plt.text(5, 5, t, ha='center', wrap=True)
```

Das Argument `wrap=True` sagt Matplotlib, den Text automatisch umzubrechen.
