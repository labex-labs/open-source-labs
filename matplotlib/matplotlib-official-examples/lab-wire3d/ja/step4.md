# プロットのカスタマイズ

プロットをより視覚的に魅力的にするためにカスタマイズできます。この例では、タイトル、軸ラベルを追加し、プロットの色を変更します。

```python
# Customize the plot
ax.set_title('Wireframe Plot')
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
ax.plot_wireframe(X, Y, Z, rstride=5, cstride=5, color='green')
```
