# グラフを保存する

`savefig` メソッドを使用して、グラフを画像ファイルとして保存することができます。次のコードは、グラフを PNG 画像として保存します。

```python
plt.plot([1, 2, 3, 4], 'o-r')
plt.title('Simple Plot')
plt.xlabel('Index')
plt.ylabel('Numbers')
plt.savefig('simple_plot.png')
```
