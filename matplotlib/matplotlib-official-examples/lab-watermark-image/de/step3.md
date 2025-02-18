# Diagramm erstellen

Jetzt können wir das Diagramm erstellen, auf das wir das Bild legen möchten. In diesem Beispiel erstellen wir ein einfaches Balkendiagramm mit zufälligen Daten.

```python
fig, ax = plt.subplots()

np.random.seed(19680801)
x = np.arange(30)
y = x + np.random.randn(30)
ax.bar(x, y, color='#6bbc6b')
ax.grid()
```
