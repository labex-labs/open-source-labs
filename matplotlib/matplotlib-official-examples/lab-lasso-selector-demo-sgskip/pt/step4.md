# Aceitar os Pontos Selecionados

Aceite os pontos selecionados usando a tecla Enter e imprima-os no console.

```python
def accept(event):
    if event.key == "enter":
        print("Selected points:")
        print(selector.xys[selector.ind])
        selector.disconnect()
        ax.set_title("")
        fig.canvas.draw()

fig.canvas.mpl_connect("key_press_event", accept)
ax.set_title("Press enter to accept selected points.")

plt.show()
```
