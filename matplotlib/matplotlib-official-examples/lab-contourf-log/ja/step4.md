# プロットをカスタマイズする

ラベル、タイトルを追加し、カラーマップを変更することでプロットをカスタマイズできます。

```python
fig, ax = plt.subplots()
cs = ax.contourf(X, Y, z, locator=ticker.LogLocator(), cmap=cm.coolwarm)

ax.set_title('Contourf Plot with Log Color Scale')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')

cbar = fig.colorbar(cs)

plt.show()
```
