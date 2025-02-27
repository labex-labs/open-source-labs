# コンセンサススコアを計算する

`consensus_score()` 関数を使用して、二部クラスタのコンセンサススコアを計算します。

```python
score = consensus_score(model.biclusters_, (rows[:, row_idx], columns[:, col_idx]))
print("consensus score: {:.3f}".format(score))
```
