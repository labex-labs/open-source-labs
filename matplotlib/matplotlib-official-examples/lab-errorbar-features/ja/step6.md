# エラーバー付きの対数スケールのプロット

最後に、対数スケールとエラーバー付きでデータをプロットします。`ax.set_yscale()`関数を使用して、y軸を対数スケールに設定します。

```python
# plot log scale with error bars
fig, ax = plt.subplots()
ax.errorbar(x, y, yerr=error, fmt='o')
ax.set_title('Log Scale with Error Bars')
ax.set_yscale('log')
plt.show()
```
