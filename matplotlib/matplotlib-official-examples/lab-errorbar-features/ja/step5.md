# 変数付き非対称エラーバーのプロット

次に、変数付き非対称エラーバー付きでデータをプロットします。再び`ax.errorbar()`関数を使用しますが、今回は`xerr`パラメータを使用して非対称誤差値を指定します。

```python
# plot variable, asymmetric error bars
fig, ax = plt.subplots()
ax.errorbar(x, y, xerr=asymmetric_error, fmt='o')
ax.set_title('Variable, Asymmetric Error Bars')
plt.show()
```
