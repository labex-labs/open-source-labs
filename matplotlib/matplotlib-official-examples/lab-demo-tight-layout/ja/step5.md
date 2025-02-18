# プロットの保存

プロットを作成したら、それをファイルに保存することができます。

```python
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y)
plt.title('My Plot')
plt.xlabel('X Axis Label')
plt.ylabel('Y Axis Label')
plt.savefig('my_plot.png')
```

ここでは、`savefig`関数を使用して、プロットを`my_plot.png`という名前のファイルに保存しています。
