# プロットにテキストを追加する

`ax.text()`関数を使って、プロットにテキストを追加できます。この例では、異なるフォントファミリでテキストを追加します。

```python
ax.text(0.5, 3., "serif", family="serif")
ax.text(0.5, 2., "monospace", family="monospace")
ax.text(2.5, 2., "sans-serif", family="sans-serif")
ax.set_xlabel(r"µ is not $\mu$")
```
