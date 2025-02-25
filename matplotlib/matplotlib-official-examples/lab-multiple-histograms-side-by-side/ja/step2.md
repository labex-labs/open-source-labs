# サンプルデータセットを作成する

次に、ヒストグラムに使用するサンプルデータセットを作成します。それぞれ387個のデータポイントを持つ3つのデータセットを作成します。

```python
np.random.seed(19680801)
number_of_data_points = 387
labels = ["A", "B", "C"]
data_sets = [np.random.normal(0, 1, number_of_data_points),
             np.random.normal(6, 1, number_of_data_points),
             np.random.normal(-3, 1, number_of_data_points)]
```
