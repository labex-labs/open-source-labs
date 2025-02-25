# プロットのカスタマイズ

`bottom` パラメータを使用して基準線を調整することで、プロットをカスタマイズできます。また、`linefmt`、`markerfmt`、`basefmt` パラメータを使用して、プロットの書式設定プロパティを調整することもできます。

```python
markerline, stemlines, baseline = plt.stem(
    x, y, linefmt='grey', markerfmt='D', bottom=1.1)
markerline.set_markerfacecolor('none')
plt.show()
```

これにより、グレーの線の書式とダイヤモンド形状のマーカーがあるプロットが生成されます。また、基準線も 1.1 に調整されています。
