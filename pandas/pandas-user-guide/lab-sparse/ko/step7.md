# scipy sparse 와 상호 작용

마지막으로, scipy sparse 행렬에서 희소 값을 가진 DataFrame 을 생성할 수 있으며, 그 반대도 가능합니다.

```python
# 필요한 라이브러리 임포트
from scipy.sparse import csr_matrix

# scipy 를 사용하여 희소 행렬 생성
arr = np.random.random(size=(1000, 5))
arr[arr < .9] = 0
sp_arr = csr_matrix(arr)

# 희소 행렬에서 DataFrame 생성
sdf = pd.DataFrame.sparse.from_spmatrix(sp_arr)

# DataFrame 출력
print(sdf.head())
print(sdf.dtypes)

# 다시 희소 행렬로 변환
print(sdf.sparse.to_coo())
```
