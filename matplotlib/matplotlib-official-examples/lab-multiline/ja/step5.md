# プロットにテキストを追加する

`text`関数を使用して、プロットにテキストを追加することができます。テキストの位置、回転、水平および垂直方向の配置、および複数行の配置を指定することができます。

```python
ax0.text(2, 7, 'this is\nyet another test',
         rotation=45,
         horizontalalignment='center',
         verticalalignment='top',
         multialignment='center')
```
