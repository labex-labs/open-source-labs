# グラフのカスタマイズ

x軸とy軸にラベルを付け、y軸の目盛りを対数に設定することで、グラフの外観をカスタマイズできます。

```python
ax.set_xticks(x + dimw / 2, labels=map(str, x))
ax.set_yscale('log')

ax.set_xlabel('x')
ax.set_ylabel('y')
```
