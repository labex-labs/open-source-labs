# 메모리 효율성 확인

다음으로, 희소 데이터 구조를 사용하는 메모리 효율성을 확인합니다. 대규모 DataFrame 을 생성하고, 이를 희소 (sparse) 로 변환한 다음 메모리 사용량을 비교합니다.

```python
# 랜덤 값으로 대규모 DataFrame 생성
df = pd.DataFrame(np.random.randn(10000, 4))

# DataFrame 의 대부분을 NaN 으로 설정
df.iloc[:9998] = np.nan

# DataFrame 을 희소로 변환
sdf = df.astype(pd.SparseDtype("float", np.nan))

# 밀집 (dense) vs 희소 DataFrame 의 메모리 사용량 확인
print('dense : {:0.2f} bytes'.format(df.memory_usage().sum() / 1e3))
print('sparse: {:0.2f} bytes'.format(sdf.memory_usage().sum() / 1e3))
```
