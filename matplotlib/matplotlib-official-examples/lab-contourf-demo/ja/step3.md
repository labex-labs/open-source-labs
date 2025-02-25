# 明示的なレベルで塗りつぶされたコントアウトの作成

次に、明示的なレベルで塗りつぶされたコントアウトプロットを作成します。`levels`パラメータを値のリストに設定してコントアウトレベルを指定するために`contourf`メソッドを使用します。また、カラーマップを色のリストに設定し、`extend`パラメータを`'both'`に設定してレベルの範囲外の値を表示します。

```python
# Create filled contour with explicit levels
fig, ax = plt.subplots()
levels = [-1.5, -1, -0.5, 0, 0.5, 1]
CS = ax.contourf(X, Y, Z, levels, colors=('r', 'g', 'b'),
                 origin=origin, extend='both')
CS2 = ax.contour(X, Y, Z, levels, colors=('k',),
                 linewidths=(3,), origin=origin)

# Add title, axis labels, and colorbar
ax.set_title('Filled Contour with Explicit Levels')
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
cbar = fig.colorbar(CS)
cbar.ax.set_ylabel('Z Label')

# Show plot
plt.show()
```
