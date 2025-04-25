# データをプロットする

このステップでは、Matplotlib の`plot`関数を使って、1 回の呼び出しですべての 3 つのデータセットをプロットします。最初のデータセットには赤い破線を、2 番目のデータセットには青い四角を、3 番目のデータセットには緑の三角形を使います。

```python
plt.plot(t, t, 'r--', label='linear')
plt.plot(t, t**2, 'bs', label='quadratic')
plt.plot(t, t**3, 'g^', label='cubic')
plt.legend()
plt.show()
```
