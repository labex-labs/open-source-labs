# 複数のグループを持つ散布図の作成

各グループをループしてそのグループ用の散布図を作成することで、複数のグループを持つ散布図を作成できます。それぞれのグループに対して、マーカーの色、サイズ、透明度をそれぞれ`c`、`s`、`alpha`パラメータを使って指定します。また、凡例に表示されるグループ名を`label`パラメータに設定します。

```python
fig, ax = plt.subplots()
for color in ['tab:blue', 'tab:orange', 'tab:green']:
    n = 750
    x, y = np.random.rand(2, n)
    scale = 200.0 * np.random.rand(n)
    ax.scatter(x, y, c=color, s=scale, label=color,
               alpha=0.3, edgecolors='none')

ax.legend()
ax.grid(True)

plt.show()
```
