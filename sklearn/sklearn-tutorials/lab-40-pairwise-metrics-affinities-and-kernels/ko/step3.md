# 코사인 유사도

코사인 유사도는 두 벡터 간의 유사성을 측정하는 방법입니다. 벡터를 정규화한 후 벡터 사이의 각도의 코사인을 계산합니다.

Scikit-learn 은 벡터 간의 코사인 유사도를 계산하기 위한 `cosine_similarity` 함수를 제공합니다.

```python
from sklearn.metrics.pairwise import cosine_similarity

X = np.array([[2, 3], [3, 5], [5, 8]])
Y = np.array([[1, 0], [2, 1]])

# X 와 Y 사이의 코사인 유사도 계산
similarity = cosine_similarity(X, Y)
print(similarity)
```

출력:

```
array([[0.89442719, 0.9486833 ],
       [0.93982748, 0.99388373],
       [0.99417134, 0.99705449]])
```
