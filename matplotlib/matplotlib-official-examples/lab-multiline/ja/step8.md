# X 軸ラベルのカスタマイズ

X 軸ラベルをカスタマイズするには、`set_xticks`関数を使用できます。目盛りの位置とラベルを指定できます。

```python
ax1.set_xticks([0.2, 0.4, 0.6, 0.8, 1.],
               labels=["Jan\n2009", "Feb\n2009", "Mar\n2009", "Apr\n2009",
                       "May\n2009"])
```
