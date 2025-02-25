# Akzeptieren der ausgewählten Punkte

Akzeptiere die ausgewählten Punkte mit der Enter-Taste und drucke sie in der Konsole aus.

```python
def accept(event):
    if event.key == "enter":
        print("Ausgewählte Punkte:")
        print(selector.xys[selector.ind])
        selector.disconnect()
        ax.set_title("")
        fig.canvas.draw()

fig.canvas.mpl_connect("key_press_event", accept)
ax.set_title("Drücken Sie Enter, um die ausgewählten Punkte zu akzeptieren.")

plt.show()
```
