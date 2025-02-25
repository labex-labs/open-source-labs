# すべての誤差棒をプロットする

次に、サブサンプリングなしで`errorbar`関数を使用してすべての誤差棒をプロットします。これがベースラインのプロットとなります。

```python
fig, ax = plt.subplots()

ax.set_title('All Errorbars')
ax.errorbar(x, y1, yerr=y1err, label='y1')
ax.errorbar(x, y2, yerr=y2err, label='y2')

ax.legend()
plt.show()
```
