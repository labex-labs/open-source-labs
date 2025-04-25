# チャートをカスタマイズする

ラベル、タイトルを追加し、x 軸の目盛りラベルと凡例を調整することで、チャートをカスタマイズできます。また、y 軸の制限を設定して、すべてのデータが表示されるようにします。

```python
ax.set_ylabel('Length (mm)')
ax.set_title('Penguin attributes by species')
ax.set_xticks(x + width, species)
ax.legend(loc='upper left', ncols=3)
ax.set_ylim(0, 250)
```
