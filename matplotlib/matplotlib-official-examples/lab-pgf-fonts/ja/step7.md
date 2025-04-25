# グラフを保存する

最後に、`fig.savefig()`関数を使ってグラフを PDF と PNG ファイルとして保存します。

```python
fig.tight_layout(pad=.5)

fig.savefig("pgf_fonts.pdf")
fig.savefig("pgf_fonts.png")
```
