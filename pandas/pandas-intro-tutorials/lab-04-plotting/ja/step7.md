# 各列に対するサブプロットを作成する

subplots 引数を使用して、各データ列に対して個別のサブプロットを作成できます。

```python
# Creating subplots for each column
axs = air_quality.plot.area(figsize=(12, 4), subplots=True)
plt.show()
```
