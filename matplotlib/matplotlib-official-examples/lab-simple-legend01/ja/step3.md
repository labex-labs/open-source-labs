# プロットに凡例を追加する

ここで、プロットに凡例を追加します。Matplotlibで凡例を追加する方法は2通りあります。この例では両方の方法を使います。

```python
# 方法1：サブプロットの上に凡例を配置する
ax.legend(bbox_to_anchor=(0., 1.02, 1.,.102), loc='lower left',
           ncols=2, mode="expand", borderaxespad=0.)

# 方法2：サブプロットの右に凡例を配置する
ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
```
