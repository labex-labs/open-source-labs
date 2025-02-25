# Aceptar los puntos seleccionados

Acepte los puntos seleccionados utilizando la tecla enter y muéstrelos en la consola.

```python
def accept(event):
    if event.key == "enter":
        print("Puntos seleccionados:")
        print(selector.xys[selector.ind])
        selector.disconnect()
        ax.set_title("")
        fig.canvas.draw()

fig.canvas.mpl_connect("key_press_event", accept)
ax.set_title("Presione enter para aceptar los puntos seleccionados.")

plt.show()
```
