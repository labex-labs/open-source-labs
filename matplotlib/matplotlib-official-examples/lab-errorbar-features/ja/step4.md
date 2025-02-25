# 変数付き対称エラーバーのプロット

次に、変数付き対称エラーバー付きでデータをプロットします。`ax.errorbar()`関数を使用してプロットを作成し、`yerr`パラメータを使用して誤差値を指定します。

```python
# plot variable, symmetric error bars
fig, ax = plt.subplots()
ax.errorbar(x, y, yerr=error, fmt='-o')
ax.set_title('Variable, Symmetric Error Bars')
plt.show()
```
