# その後の文字列を作成する

次のステップは、`~.Axes.annotate` を使ってその後の文字列を作成することです。この関数を使うことで、前の文字列に対して文字列を配置することができます。以下のコードは、前の文字列の右に配置される 3 つの文字列を作成します。

```python
text = ax.annotate(
    " says,", xycoords=text, xy=(1, 0), verticalalignment="bottom",
    color="gold", weight="bold")  # custom properties
text = ax.annotate(
    " hello", xycoords=text, xy=(1, 0), verticalalignment="bottom",
    color="green", style="italic")  # custom properties
text = ax.annotate(
    " world!", xycoords=text, xy=(1, 0), verticalalignment="bottom",
    color="blue", family="serif")  # custom properties
```
