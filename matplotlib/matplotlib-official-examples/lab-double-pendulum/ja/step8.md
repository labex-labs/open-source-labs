# アニメーションを作成する

次に、MatplotlibのFuncAnimation関数を使ってアニメーションを作成します。

```python
ani = animation.FuncAnimation(
    fig, animate, len(y), interval=dt*1000, blit=True)
plt.show()
```
