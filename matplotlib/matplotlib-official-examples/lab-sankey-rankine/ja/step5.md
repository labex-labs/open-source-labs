# ラベルとフォーマットを追加する

サンキー図のパッチに対して、各パッチの`text`属性を使ってラベルを追加します。また、テキストを太字にフォーマットし、フォントサイズを大きくします。

```python
diagrams = sankey.finish()
for diagram in diagrams:
    diagram.text.set_fontweight('bold')
    diagram.text.set_fontsize('10')
    for text in diagram.texts:
        text.set_fontsize('10')
```
