# サブプロットを作成する

Matplotlibでサブプロットを作成するには、`subplot()` メソッドを使用できます。このメソッドは3つの引数をとります。行数、列数、およびプロット番号です。以下は、3つのサブプロットを作成する例です：

```python
plt.subplot(311)
plt.plot([1, 2, 3])

plt.subplot(312)
plt.plot([1, 2, 3])
plt.grid(True)

plt.subplot(313)
plt.plot([1, 2, 3])
plt.grid(True)
```
