# Erzeuge den Graphen und verbinde den Tastendruck-Ereignis-Listener

Wir erstellen einen einfachen Graphen, indem wir `np.random.rand()` verwenden, um zufällige Daten zu generieren. Anschließend setzen wir den Tastendruck-Ereignis-Listener mit `fig.canvas.mpl_connect()` ein und übergeben den Namen des Ereignisses, auf das wir lauschen möchten (`'key_press_event'`), und die Funktion, die aufgerufen werden soll, wenn das Ereignis eintritt (`on_press`).

```python
fig, ax = plt.subplots()

fig.canvas.mpl_connect('key_press_event', on_press)

ax.plot(np.random.rand(12), np.random.rand(12), 'go')
xl = ax.set_xlabel('easy come, easy go')
ax.set_title('Press a key')
plt.show()
```
