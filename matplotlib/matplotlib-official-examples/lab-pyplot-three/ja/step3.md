# データをプロットする

このステップでは、Matplotlibの`plot`関数を使って、1回の呼び出しですべての3つのデータセットをプロットします。最初のデータセットには赤い破線を、2番目のデータセットには青い四角を、3番目のデータセットには緑の三角形を使います。

```python
plt.plot(t, t, 'r--', label='linear')
plt.plot(t, t**2, 'bs', label='quadratic')
plt.plot(t, t**3, 'g^', label='cubic')
plt.legend()
plt.show()
```
