# SkewT - logP 図を作成する

ここでは、先ほど登録した SkewXAxes 射影を使って SkewT - logP 図を作成します。まず、figure オブジェクトを作成し、SkewXAxes 射影付きのサブプロットを追加します。その後、semilogy 関数を使って温度と露点データを図にプロットします。最後に、X 軸と Y 軸の範囲と目盛りを設定し、プロットを表示します。

```python
fig = plt.figure(figsize=(6.5875, 6.2125))
ax = fig.add_subplot(projection='skewx')

ax.semilogy(T, p, color='C3')
ax.semilogy(Td, p, color='C2')

ax.axvline(0, color='C0')

ax.yaxis.set_major_formatter(ScalarFormatter())
ax.yaxis.set_minor_formatter(NullFormatter())
ax.set_yticks(np.linspace(100, 1000, 10))
ax.set_ylim(1050, 100)

ax.xaxis.set_major_locator(MultipleLocator(10))
ax.set_xlim(-50, 50)

plt.grid(True)
plt.show()
```
