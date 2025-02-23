# Erstellen des Diagramms

Lassen Sie uns ein einfaches Liniendiagramm mit einigen langen y-Beschriftungen erstellen.

```python
fig, ax = plt.subplots()
ax.plot(range(10))
ax.set_yticks([2, 5, 7], labels=['really, really, really', 'long', 'labels'])
```
