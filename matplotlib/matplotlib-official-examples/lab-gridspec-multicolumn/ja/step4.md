# GridSpecにサブプロットを追加する

`fig.add_subplot()` 関数を使用して、GridSpecにサブプロットを追加できます。GridSpecオブジェクトのインデックス表記を使用して、グリッド内のサブプロットの位置を指定できます。たとえば、`gs[0, :]` は1行目とすべての列を指定します。

```python
ax1 = fig.add_subplot(gs[0, :])
ax2 = fig.add_subplot(gs[1, :-1])
ax3 = fig.add_subplot(gs[1:, -1])
ax4 = fig.add_subplot(gs[-1, 0])
ax5 = fig.add_subplot(gs[-1, -2])
```
