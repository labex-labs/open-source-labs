# グラフを作成してキー入力イベントリスナーを接続する

`np.random.rand()` を使ってランダムなデータを生成し、簡単なグラフを作成します。そして、`fig.canvas.mpl_connect()` を使ってキー入力イベントリスナーを設定し、リッスンするイベントの名前 (`'key_press_event'`) とイベントが発生したときに呼び出す関数 (`on_press`) を渡します。

```python
fig, ax = plt.subplots()

fig.canvas.mpl_connect('key_press_event', on_press)

ax.plot(np.random.rand(12), np.random.rand(12), 'go')
xl = ax.set_xlabel('easy come, easy go')
ax.set_title('Press a key')
plt.show()
```
