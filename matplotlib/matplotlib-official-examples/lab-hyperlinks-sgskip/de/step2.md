# Erstellen eines Streudiagramms mit Hyperlinks

In diesem Schritt werden wir ein Streudiagramm erstellen und Hyperlinks zu den Markern hinzufügen. Hier ist der Code, um das Streudiagramm zu erstellen:

```python
fig = plt.figure()
s = plt.scatter([1, 2, 3], [4, 5, 6])
```

Um Hyperlinks hinzuzufügen, müssen wir die `set_urls()`-Methode des Streudiagramm-Objekts verwenden. Diese Methode nimmt eine Liste von URLs als Argument entgegen. Hier ist der aktualisierte Code:

```python
s.set_urls(['https://www.bbc.com/news', 'https://www.google.com/', None])
```

Die ersten beiden Marker werden jeweils einen Hyperlink zu `https://www.bbc.com/news` und `https://www.google.com/` haben. Der dritte Marker wird keinen Hyperlink haben. Schließlich können wir das Diagramm als SVG-Datei speichern, indem wir `fig.savefig()` verwenden:

```python
fig.savefig('scatter.svg')
```
