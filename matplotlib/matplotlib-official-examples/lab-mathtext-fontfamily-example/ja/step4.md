# タイトルのフォントを設定する

`math_fontfamily` パラメータを使用して、タイトルのフォントファミリを変更することもできます。

```python
ax.set_title(r"数式モードのタイトル: \int_{0}^{\infty } x^2 dx",
             math_fontfamily='stixsans', size=14)
```
