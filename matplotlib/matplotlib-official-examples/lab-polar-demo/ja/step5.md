# グラフをカスタマイズする

グラフをカスタマイズするには、次の方法を使用できます。

- `set_rmax` で `r` の最大値を設定する
- `set_rticks` で `r` の目盛り値を設定する
- `set_rlabel_position` で半径方向のラベルの位置を設定する

```python
ax.set_rmax(2)
ax.set_rticks([0.5, 1, 1.5, 2])
ax.set_rlabel_position(-22.5)
```

また、`set_title` メソッドを使ってグラフにタイトルを追加することもできます。

```python
ax.set_title("A line plot on a polar axis", va='bottom')
```

最後に、`grid` メソッドを使ってグラフにグリッドを追加することができます。

```python
ax.grid(True)
```
