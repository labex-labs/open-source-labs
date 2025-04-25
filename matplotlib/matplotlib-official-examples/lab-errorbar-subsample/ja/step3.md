# 6 番目の誤差棒ごとにサブサンプリングする

次に、誤差棒サブサンプリングを適用して、6 番目の誤差棒のみをプロットしましょう。これは、`errorbar`関数の`errorevery`パラメータを使用することで行えます。

```python
fig, ax = plt.subplots()

ax.set_title('Every 6th Errorbar')
ax.errorbar(x, y1, yerr=y1err, errorevery=6, label='y1')
ax.errorbar(x, y2, yerr=y2err, errorevery=6, label='y2')

ax.legend()
plt.show()
```
