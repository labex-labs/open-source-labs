# グラフをカスタマイズする

グラフをより情報豊かにするために、ラベルやタイトルを追加したり、y 軸を反転させたりすることでカスタマイズできます。

```python
ax.set_yticks(y_pos, labels=people)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel('Performance')
ax.set_title('How fast do you want to go today?')
```
