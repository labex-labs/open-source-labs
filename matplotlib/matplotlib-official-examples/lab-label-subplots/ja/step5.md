# タイトル付きのラベル

もし我々がラベルをタイトルと整列させたい場合、我々はそれをタイトルに組み込むか、または `loc` キーワード引数を使用することができます。

```python
for label, ax in axs.items():
    ax.set_title('Normal Title', fontstyle='italic')
    ax.set_title(label, fontfamily='serif', loc='left', fontsize='medium')
```
