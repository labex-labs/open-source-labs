# 二次y軸を作成する

データからの即興的な変換で軸を関連付ける例を3つ目に作成します。この変換は経験的に導き出されます。この場合、順方向と逆方向の変換関数を、一方のデータセットからもう一方のデータセットへの線形補間に設定します。

```python
fig, ax = plt.subplots(layout='constrained')
xdata = np.arange(1, 11, 0.4)
ydata = np.random.randn(len(xdata))
ax.plot(xdata, ydata, label='Plotted data')

xold = np.arange(0, 11, 0.2)
# 別のデータに基づく座標にx座標を関連付ける疑似データセット。
# xnewは単調増加でなければならないので、ソートします...
xnew = np.sort(10 * np.exp(-xold / 4) + np.random.randn(len(xold)) / 3)

ax.plot(xold[3:], xnew[3:], label='Transform data')
ax.set_xlabel('X [m]')
ax.legend()

def forward(x):
    return np.interp(x, xold, xnew)

def inverse(x):
    return np.interp(x, xnew, xold)

secax = ax.secondary_xaxis('top', functions=(forward, inverse))
secax.xaxis.set_minor_locator(AutoMinorLocator())
secax.set_xlabel('$X_{other}$')
```
