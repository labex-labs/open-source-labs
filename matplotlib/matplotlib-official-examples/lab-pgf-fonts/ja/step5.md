# グラフにテキストを追加する

`ax.text()`関数を使ってグラフにテキストを追加します。グラフの 4 つの異なる場所に、それぞれ異なるフォントファミリ（セリフ、等幅、ゴシック、草書体）でテキストを追加します。

```python
ax.text(0.5, 3., "serif")
ax.text(0.5, 2., "monospace", family="monospace")
ax.text(2.5, 2., "sans-serif", family="DejaVu Sans")
ax.text(2.5, 1., "comic", family="cursive")
```
