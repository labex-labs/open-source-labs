# グラフをカスタマイズする

軸のラベルとタイトルを追加することで、グラフをさらにカスタマイズできます。また、軸のラベルや凡例のタイトルの色を変更することもできます。以下のコードはグラフをカスタマイズする方法を示しています。

```python
fig, ax = plt.subplots()
ax.bar(fruits, counts, label=bar_labels, color=bar_colors)
ax.set_ylabel('fruit supply', color='blue')
ax.set_xlabel('fruit names', color='blue')
ax.set_title('Fruit supply by kind and color', color='purple')
ax.legend(title='Fruit color', title_color='red', labelcolor='green')
plt.show()
```
