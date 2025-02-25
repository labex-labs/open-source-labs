# 自動レベルで塗りつぶされたコントアウトの作成

次に、自動レベルで塗りつぶされたコントアウトプロットを作成します。`cmap`パラメータを`plt.cm.bone`に設定してカラーマップを指定するために`contourf`メソッドを使用します。また、`contour`メソッドを使ってコントアウト線を追加し、塗りつぶされたコントアウトに使用されるコントアウトレベルのサブセットを渡します。

```python
# Create filled contour with automatic levels
fig, ax = plt.subplots()
CS = ax.contourf(X, Y, Z, 10, cmap=plt.cm.bone, origin=origin)
CS2 = ax.contour(CS, levels=CS.levels[::2], colors='r', origin=origin)

# Add title, axis labels, and colorbar
ax.set_title('Filled Contour with Automatic Levels')
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
cbar = fig.colorbar(CS)
cbar.ax.set_ylabel('Z Label')
cbar.add_lines(CS2)

# Show plot
plt.show()
```
