# 選択された点を受け付ける

エンターキーを使って選択された点を受け付け、コンソールに表示します。

```python
def accept(event):
    if event.key == "enter":
        print("選択された点：")
        print(selector.xys[selector.ind])
        selector.disconnect()
        ax.set_title("")
        fig.canvas.draw()

fig.canvas.mpl_connect("key_press_event", accept)
ax.set_title("選択された点を受け付けるにはエンターキーを押してください。")

plt.show()
```
