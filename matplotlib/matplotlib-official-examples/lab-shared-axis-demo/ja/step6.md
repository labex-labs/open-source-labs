# 目盛りラベルを削除する

特定のサブプロットから目盛りラベルを削除するには、`ax.get_xticklabels()` メソッドを使ってラベルの表示を変更します。この例では、2 番目のサブプロットの x 軸の目盛りラベルを削除します。

```python
plt.tick_params('x', labelbottom=False)
```
