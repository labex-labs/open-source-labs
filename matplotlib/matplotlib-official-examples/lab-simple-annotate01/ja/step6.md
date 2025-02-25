# 注釈のカスタマイズ

フォントサイズ、フォントカラー、矢印スタイルを変更することで、注釈をカスタマイズできます。次のコードでは、テキスト注釈のフォントサイズ、フォントカラー、矢印スタイルを変更します。

```python
ax.annotate("Data Point 1", xy=(1, 3), xytext=(1.5, 3.5),
            arrowprops=dict(facecolor="black", shrink=0.05, arrowstyle="->"),
            fontsize=12, color="red")
```
