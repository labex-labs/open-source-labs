# 棒グラフを作成する

ここで、手順2で定義したデータを使って棒グラフを作成できます。Matplotlibの`pyplot`モジュールの`bar()`メソッドを使ってグラフを作成します。また、凡例のエントリと棒の色をそれぞれ制御するために、`label`と`color`パラメータを渡します。以下のコードは棒グラフを作成する方法を示しています。

```python
fig, ax = plt.subplots()
ax.bar(fruits, counts, label=bar_labels, color=bar_colors)
ax.set_ylabel('fruit supply')
ax.set_title('Fruit supply by kind and color')
ax.legend(title='Fruit color')
plt.show()
```
