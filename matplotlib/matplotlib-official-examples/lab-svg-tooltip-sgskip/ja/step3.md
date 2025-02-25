# グラフをSVG形式で保存する

`BytesIO` クラスと `savefig` メソッドを使って、グラフを偽のファイルオブジェクトに保存します。

```python
ax.set_xlim(-30, 30)
ax.set_ylim(-30, 30)
ax.set_aspect('equal')

f = BytesIO()
plt.savefig(f, format="svg")
```
