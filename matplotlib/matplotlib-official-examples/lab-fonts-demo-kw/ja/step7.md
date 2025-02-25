# 太字と斜体を表示する

付け加えとして、太字と斜体の両方のスタイルを持つテキストも表示できます。適切なスタイル、太さ、サイズでテキストを表示するために、`fig.text()` メソッドを使用します。

```python
fig.text(0.3, 0.1, 'bold italic',
         style='italic', weight='bold', size='x-small', **alignment)
fig.text(0.3, 0.2, 'bold italic',
         style='italic', weight='bold', size='medium', **alignment)
fig.text(0.3, 0.3, 'bold italic',
         style='italic', weight='bold', size='x-large', **alignment)
```
