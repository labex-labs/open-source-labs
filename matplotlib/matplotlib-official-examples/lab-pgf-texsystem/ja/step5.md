# レイアウトを調整してプロットを保存する

最後に、それぞれ`fig.tight_layout()`と`fig.savefig()`関数を使って、プロットのレイアウトを調整してファイルに保存することができます。

```python
fig.tight_layout(pad=.5)

fig.savefig("pgf_texsystem.pdf")
fig.savefig("pgf_texsystem.png")
```
