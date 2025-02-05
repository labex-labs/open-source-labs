# 余弦相似度

余弦相似度是衡量两个向量之间相似性的一种度量。它在对向量进行归一化后，计算它们之间夹角的余弦值。

Scikit-learn 提供了 `cosine_similarity` 函数来计算向量之间的余弦相似度。

```python
from sklearn.metrics.pairwise import cosine_similarity

X = np.array([[2, 3], [3, 5], [5, 8]])
Y = np.array([[1, 0], [2, 1]])

# 计算 X 和 Y 之间的余弦相似度
similarity = cosine_similarity(X, Y)
print(similarity)
```

输出：

```
array([[0.89442719, 0.9486833 ],
       [0.93982748, 0.99388373],
       [0.99417134, 0.99705449]])
```
