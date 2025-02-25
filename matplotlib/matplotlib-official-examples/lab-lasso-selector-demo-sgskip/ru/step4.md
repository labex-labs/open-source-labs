# Принять выбранные точки

Принимайте выбранные точки с помощью клавиши Enter и выводите их в консоль.

```python
def accept(event):
    if event.key == "enter":
        print("Выбранные точки:")
        print(selector.xys[selector.ind])
        selector.disconnect()
        ax.set_title("")
        fig.canvas.draw()

fig.canvas.mpl_connect("key_press_event", accept)
ax.set_title("Нажмите Enter, чтобы принять выбранные точки.")

plt.show()
```
