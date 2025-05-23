# サブプロットを作成する

`.pyplot.subplot`を使用して、2 つのサブプロット付きの図を作成します。

```python
plt.figure()

plt.subplot(211)
plt.plot(t1, f(t1), color='tab:blue', marker='o')
plt.plot(t2, f(t2), color='black')

plt.subplot(212)
plt.plot(t2, np.cos(2*np.pi*t2), color='tab:orange', linestyle='--')

plt.show()
```

`subplot()`関数は 3 つの引数をとります。行数、列数、および現在のプロットのインデックスです。インデックスは左上隅から 1 から始まり、行方向に増加します。この例では、2 つのサブプロット付きの図を作成します。上に 1 つと下に 1 つです。

最初のサブプロットでは、`t1`に対して`f(t1)`をプロットし、`t2`に対して`f(t2)`をプロットします。最初のプロットの色を青に設定し、各データポイントに円形のマーカーを追加します。2 番目のプロットの色を黒に設定します。

2 番目のサブプロットでは、`t2`に対して`2*np.pi*t2`の余弦関数をプロットします。プロットの色をオレンジに設定し、線のスタイルを破線に設定します。
