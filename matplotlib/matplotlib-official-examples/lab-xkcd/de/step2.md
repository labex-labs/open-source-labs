# Erstellen eines xkcd-stils Diagramms

In diesem Schritt werden wir ein xkcd-styles Diagramm erstellen, das die Beziehung zwischen Zeit und allgemeiner Gesundheit zeigt. Das Diagramm basiert auf der Comicserie "Stove Ownership" von XKCD.

```python
with plt.xkcd():
    fig = plt.figure()
    ax = fig.add_axes((0.1, 0.2, 0.8, 0.7))
    ax.spines[['top', 'right']].set_visible(False)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_ylim([-30, 10])

    data = np.ones(100)
    data[70:] -= np.arange(30)

    ax.annotate(
        'DER TAG, AN DEM ICH MERKTE,\nDASS ICH BACON KOCKEN KONNE\nWENN ICH WILL',
        xy=(70, 1), arrowprops=dict(arrowstyle='->'), xytext=(15, -10))

    ax.plot(data)

    ax.set_xlabel('time')
    ax.set_ylabel('my overall health')
    fig.text(
        0.5, 0.05,
        '"Stove Ownership" from xkcd by Randall Munroe',
        ha='center')

plt.show()
```
