# `.plot()` を使ってグラフを描画する

`.plot()` 関数の `drawstyle` パラメータを使うことで、`.step()` と同じ動作を実現することができます。異なる `drawstyle` の値を使って 3 つのグラフを作成します。

```python
plt.plot(x, y + 2, drawstyle='steps', label='steps (=steps-pre)')
plt.plot(x, y + 1, drawstyle='steps-mid', label='steps-mid')
plt.plot(x, y, drawstyle='steps-post', label='steps-post')
plt.legend()
plt.show()
```

上記のコードは、それぞれ異なる `drawstyle` の値を持つ 3 つの区間定数曲線を持つグラフを作成します。
