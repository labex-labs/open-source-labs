# ラベルとタイトルを追加する

グラフにラベルとタイトルを追加することは、情報をより多く含めるために欠かせないことです。次のコードは、グラフにタイトルを追加し、x 軸と y 軸にラベルを追加します。

```python
plt.plot([1, 2, 3, 4], 'o-r')
plt.title('Simple Plot')
plt.xlabel('Index')
plt.ylabel('Numbers')
plt.show()
```
