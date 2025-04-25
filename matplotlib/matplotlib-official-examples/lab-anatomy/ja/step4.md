# ラベルとタイトルの追加

次に、`set_xlabel()`、`set_ylabel()`、および `set_title()` メソッドを使用して、x 軸と y 軸にラベルを追加し、グラフにタイトルを追加します。

```python
# Add labels and title
ax.set_xlabel("x Axis label", fontsize=14)
ax.set_ylabel("y Axis label", fontsize=14)
ax.set_title("Anatomy of a figure", fontsize=20, verticalalignment='bottom')
```
