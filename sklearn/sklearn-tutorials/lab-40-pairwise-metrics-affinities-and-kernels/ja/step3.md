# コサイン類似度

コサイン類似度は、2つのベクトル間の類似度の尺度です。ベクトルを正規化した後、それらの間の角度のコサインを計算します。

Scikit-learn は、ベクトル間のコサイン類似度を計算する `cosine_similarity` 関数を提供しています。

```python
from sklearn.metrics.pairwise import cosine_similarity

X = np.array([[2, 3], [3, 5], [5, 8]])
Y = np.array([[1, 0], [2, 1]])

# Compute cosine similarity between X and Y
similarity = cosine_similarity(X, Y)
print(similarity)
```

出力：

```
array([[0.89442719, 0.9486833 ],
       [0.93982748, 0.99388373],
       [0.99417134, 0.99705449]])
```
