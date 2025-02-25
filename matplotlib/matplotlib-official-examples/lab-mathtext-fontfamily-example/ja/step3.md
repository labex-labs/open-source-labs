# グラフ内のテキストを設定する

次に、`text()` 関数を使用してグラフ内のテキストを設定します。各個々のテキスト要素のフォントファミリを変更するために、`math_fontfamily` パラメータを使用します。

```python
# 通常のテキストと数式のテキストを混ぜたもの。
msg = (r"通常のテキスト。数式モードのテキスト: "
       r"\int_{0}^{\infty } x^2 dx")

# グラフ内にテキストを設定する。
ax.text(1, 7, msg, size=12, math_fontfamily='cm')

# 次のテキストに別のフォントを設定する。
ax.text(1, 3, msg, size=12, math_fontfamily='dejavuserif')
```
