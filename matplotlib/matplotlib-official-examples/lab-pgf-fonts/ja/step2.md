# フォントファミリを設定する

`font.family`パラメータを使用して、フォントファミリを「serif」に設定します。また、既定のLaTeXのセリフフォントを使用するために、`font.serif`パラメータを空のリストに設定します。

```python
plt.rcParams.update({
    "font.family": "serif",
    "font.serif": [],
})
```
