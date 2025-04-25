# 棒グラフを作成する

Matplotlib は棒グラフも作成できます。以下は例です。

```python
x = ['A', 'B', 'C', 'D', 'E']
y = [3, 7, 1, 9, 4]

plt.bar(x, y)
plt.xlabel('Category')
plt.ylabel('Value')
plt.title('Bar Plot')
plt.show()
```
