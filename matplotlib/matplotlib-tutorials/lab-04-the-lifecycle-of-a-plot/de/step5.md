# Anpassen des Diagrammaussehens

Wir können das Aussehen unseres Diagramms weiter anpassen. Folgen Sie diesen Schritten:

1. Drehen Sie die Beschriftungen der x-Achse, um sie lesbarer zu machen.

```python
labels = ax.get_xticklabels()
plt.setp(labels, rotation=45, horizontalalignment='right')
```

2. Legen Sie die Grenzen, die Beschriftungen und den Titel der x- und y-Achse fest.

```python
ax.set(xlim=[-10000, 140000],
       xlabel='Total Revenue',
       ylabel='Company',
       title='Company Revenue')
```

3. Zeigen Sie das Diagramm erneut an.

```python
fig, ax = plt.subplots()
ax.barh(group_names, group_data)
labels = ax.get_xticklabels()
plt.setp(labels, rotation=45, horizontalalignment='right')
ax.set(xlim=[-10000, 140000], xlabel='Total Revenue', ylabel='Company',
       title='Company Revenue')
```
