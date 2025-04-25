# 散布図

2 つのカテゴリ変数間の関係を示すために、散布図も作成できます。この場合、同じ果物データを使用し、個数にいくらかのランダムノイズを加えて、2 番目の変数を作成します。

```python
noise = np.random.rand(len(values)) * 5
plt.scatter(names, values + noise)
plt.title('Fruit Counts with Noise')
plt.xlabel('Fruit')
plt.ylabel('Count')
plt.show()
```
