# ラベルとタイトルを追加する

最後に、ボックスプロットにラベルとタイトルを追加して、情報が豊富になるようにします。x 軸と y 軸にラベルを追加し、プロットにタイトルを追加できます。また、ラベルとタイトルのフォントサイズとスタイルを変更することもできます。以下は、ラベルとタイトルを追加する方法の例です。

```python
plt.boxplot([data1, data2, data3])
plt.xlabel('Group')
plt.ylabel('Value')
plt.title('Comparison of Three Groups')
plt.xticks([1, 2, 3], ['Group 1', 'Group 2', 'Group 3'])
plt.show()
```
