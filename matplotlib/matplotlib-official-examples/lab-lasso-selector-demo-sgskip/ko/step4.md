# 선택된 점 수락

Enter 키를 사용하여 선택된 점을 수락하고 콘솔에 출력합니다.

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
