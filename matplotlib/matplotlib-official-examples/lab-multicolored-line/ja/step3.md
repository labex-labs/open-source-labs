# 線分の作成

それぞれに色付けを行うことができるように、線分のセットを作成します。2 つの配列 `points[:-1]` と `points[1:]` を 2 次元目の軸に沿って連結するために、numpy の `concatenate` 関数を使用します。その後、得られた配列を N x 1 x 2 の配列に整形して、点を簡単に積み重ねて線分を取得できるようにします。線のコレクション用の `segments` 配列は、(numlines) x (1 本の線あたりの点数) x 2（x と y のため）でなければなりません。

```python
points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)
```
