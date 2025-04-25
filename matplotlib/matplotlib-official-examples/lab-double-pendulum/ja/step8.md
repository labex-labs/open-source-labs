# アニメーションを作成する

次に、Matplotlib の FuncAnimation 関数を使ってアニメーションを作成します。

```python
ani = animation.FuncAnimation(
    fig, animate, len(y), interval=dt*1000, blit=True)
plt.show()
```
