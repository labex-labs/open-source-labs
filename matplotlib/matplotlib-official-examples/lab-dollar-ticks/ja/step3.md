# ドル記号で y 軸のラベルをフォーマットする

では、y 軸のラベルをドル記号で表示するようにフォーマットしましょう。ラベルをフォーマットするために、`matplotlib.ticker` モジュールの `StrMethodFormatter` クラスを使用します。

```python
import matplotlib.ticker as ticker

# Format y-axis labels with dollar signs
fmt = '${x:,.2f}'
tick = ticker.StrMethodFormatter(fmt)
ax.yaxis.set_major_formatter(tick)
```

上記のコードでは、フォーマット文字列 `'${x:,.2f}'` を使用して `StrMethodFormatter` オブジェクトを作成しています。このフォーマット文字列は、ドル記号の後にスペース、その後に小数点以下 2 桁のカンマ区切りの数値を表示することを指定しています。

次に、先ほど作成した `StrMethodFormatter` オブジェクトを使用して `Tick` オブジェクトを作成します。最後に、y 軸の主目盛りフォーマッタを `Tick` オブジェクトに設定します。
