# Erstellen einer Figur und eines Teilplots

Wir müssen eine Figur und einen Teilplot erstellen, um unsere Daten zu visualisieren. Wir werden einen Plot mit zwei Teilplots erstellen.

```python
fig = plt.figure()

ax = fig.add_subplot(211)
ax.plot([1, 2, 3], label="test1")
ax.plot([3, 2, 1], label="test2")

ax = fig.add_subplot(223)
ax.plot([1, 2, 3], label="test1")
ax.plot([3, 2, 1], label="test2")
```
