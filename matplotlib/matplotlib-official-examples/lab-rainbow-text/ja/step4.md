# プロットを表示する

すべての文字列を作成してカスタマイズしたら、`plt.show()` を使ってプロットを表示できます。以下のコードブロックに、プロットの完全なコードを示します。

```python
import matplotlib.pyplot as plt

plt.rcParams["font.size"] = 20
ax = plt.figure().add_subplot(xticks=[], yticks=[])

# text() で作成した最初の単語。
text = ax.text(.1,.5, "Matplotlib", color="red")
# その後の単語は、annotate() を使って前の単語に対して配置されます。
text = ax.annotate(
    " says,", xycoords=text, xy=(1, 0), verticalalignment="bottom",
    color="gold", weight="bold")  # カスタムプロパティ
text = ax.annotate(
    " hello", xycoords=text, xy=(1, 0), verticalalignment="bottom",
    color="green", style="italic")  # カスタムプロパティ
text = ax.annotate(
    " world!", xycoords=text, xy=(1, 0), verticalalignment="bottom",
    color="blue", family="serif")  # カスタムプロパティ

plt.show()
```
