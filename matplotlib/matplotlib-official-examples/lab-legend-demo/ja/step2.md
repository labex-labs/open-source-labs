# より複雑なラベルをプロットする

このステップでは、より複雑なラベルをプロットします。

```python
# グラフ用のデータを定義
x = np.linspace(0, 1)

# 複数の線を持つグラフを作成
fig, (ax0, ax1) = plt.subplots(2, 1)
for n in range(1, 5):
    ax0.plot(x, x**n, label=f"{n=}")

# 複数列とタイトル付きの凡例を作成
leg = ax0.legend(loc="upper left", bbox_to_anchor=[0, 1],
                 ncols=2, shadow=True, title="Legend", fancybox=True)
leg.get_title().set_color("red")

# 複数の線とマーカーを持つグラフを作成
ax1.plot(x, x**2, label="multi\nline")
half_pi = np.linspace(0, np.pi / 2)
ax1.plot(np.sin(half_pi), np.cos(half_pi), label=r"$\frac{1}{2}\pi$")
ax1.plot(x, 2**(x**2), label="$2^{x^2}$")

# 影付きの凡例を作成
ax1.legend(shadow=True, fancybox=True)

# グラフを表示
plt.show()
```
