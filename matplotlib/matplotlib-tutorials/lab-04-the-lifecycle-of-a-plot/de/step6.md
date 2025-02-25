# Mehrere Visualisierungen kombinieren

Wir können zusätzliche Diagrammelemente zu unserer Visualisierung hinzufügen. Folgen Sie diesen Schritten:

1. Fügen Sie eine vertikale Linie hinzu, die den Mittelwert der Verkaufsdaten darstellt.

```python
ax.axvline(group_mean, ls='--', color='r')
```

2. Kennzeichnen Sie neue Unternehmen im Diagramm.

```python
for group in [3, 5, 8]:
    ax.text(145000, group, "New Company", fontsize=10, verticalalignment="center")
```

3. Anpassen der Position des Diagrammtitels.

```python
ax.title.set(y=1.05)
```

4. Der vollständige Code ist unten dargestellt.

```python
fig, ax = plt.subplots(figsize=(8, 8))
ax.barh(group_names, group_data)
labels = ax.get_xticklabels()
plt.setp(labels, rotation=45, horizontalalignment='right')

# Add a vertical line, here we set the style in the function call
ax.axvline(group_mean, ls='--', color='r')

# Annotate new companies
for group in [3, 5, 8]:
    ax.text(145000, group, "New Company", fontsize=10,
            verticalalignment="center")

# Now we move our title up since it's getting a little cramped
ax.title.set(y=1.05)

ax.set(xlim=[-10000, 140000], xlabel='Total Revenue', ylabel='Company',
       title='Company Revenue')

plt.show()
```
