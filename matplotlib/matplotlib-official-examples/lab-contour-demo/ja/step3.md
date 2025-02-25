# ラベル付きの単純なコントアープロットを作成する

データができたので、デフォルトの色を使ってラベル付きの単純なコントアープロットを作成できます。

```python
fig, ax = plt.subplots()
CS = ax.contour(X, Y, Z)
ax.clabel(CS, inline=True, fontsize=10)
ax.set_title('Simplest default with labels')
```
