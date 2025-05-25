# 데이터 연산

데이터프레임에 정렬, 함수 적용 등과 같은 연산을 수행할 수 있습니다.

```python
# 축을 기준으로 정렬
df.sort_index(axis=1, ascending=False)

# 데이터에 함수 적용
df.apply(np.cumsum)
```
