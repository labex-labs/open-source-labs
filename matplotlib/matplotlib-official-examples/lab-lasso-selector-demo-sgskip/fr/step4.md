# Accepter les points sélectionnés

Acceptez les points sélectionnés en utilisant la touche Entrée et affichez-les dans la console.

```python
def accept(event):
    if event.key == "enter":
        print("Points sélectionnés :")
        print(selector.xys[selector.ind])
        selector.disconnect()
        ax.set_title("")
        fig.canvas.draw()

fig.canvas.mpl_connect("key_press_event", accept)
ax.set_title("Appuyez sur Entrée pour accepter les points sélectionnés.")

plt.show()
```
