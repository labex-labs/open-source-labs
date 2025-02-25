# `.step()` を使ってグラフを描画する

`.step()` 関数を使って、区間定数曲線を作成することができます。`where` パラメータは、ステップを描画する場所を決定します。異なる `where` の値を使って3つのグラフを作成します。

```python
plt.step(x, y + 2, label='pre (default)', where='pre')
plt.step(x, y + 1, label='mid', where='mid')
plt.step(x, y, label='post', where='post')
plt.legend()
plt.show()
```

上記のコードは、それぞれ異なる `where` の値を持つ3つの区間定数曲線を持つグラフを作成します。
