# カスタム フィギュア サブクラスを使ってデータをプロットする

カスタム フィギュア サブクラス `WatermarkFigure` を使って、`plt.figure()` 関数を使ってデータをプロットします。この例では、プロットに "draft" というウォーターマーク テキストを追加します。

```python
plt.figure(FigureClass=WatermarkFigure, watermark='draft')
plt.plot(x, y)
```
