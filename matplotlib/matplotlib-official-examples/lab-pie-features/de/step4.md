# Etiketten zu den Sektoren hinzufügen

Wir können den Sektoren Etiketten hinzufügen, indem wir eine Liste von Etiketten an den `labels`-Parameter der `pie()`-Funktion übergeben.

```python
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct='%1.1f%%')
```
