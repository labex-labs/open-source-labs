# グラフのカスタマイズ

これで基本的なグラフを作成しましたので、見た目を魅力的にするためにカスタマイズしましょう。タイトル、軸のラベルを追加し、線の色とスタイルを変更できます。

```python
# Add title and axis labels
plt.title('Sin Wave')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Change color and style of line
plt.plot(x, y, color='red', linestyle='dashed')
plt.show()
```
