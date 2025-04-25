# 2 番目の y 軸の目盛りラベルを設定する

2 番目の y 軸の目盛りラベルを設定するには、`set_xticks`関数を使って、目盛りの位置とラベルを引数として渡します。

```python
ax2.set_xticks([0.,.5*np.pi, np.pi, 1.5*np.pi, 2*np.pi],
               labels=["$0$", r"$\frac{1}{2}\pi$",
                       r"$\pi$", r"$\frac{3}{2}\pi$", r"$2\pi$"])
```
