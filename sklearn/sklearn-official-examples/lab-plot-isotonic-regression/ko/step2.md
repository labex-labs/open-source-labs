# 데이터 생성

다음으로, 회귀에 사용할 데이터를 생성합니다. 이 데이터는 이분산 (homoscedastic) 균일 노이즈를 가진 비선형 단조 추세를 갖도록 생성됩니다.

```python
n = 100
x = np.arange(n)
rs = check_random_state(0)
y = rs.randint(-50, 50, size=(n,)) + 50.0 * np.log1p(np.arange(n))
```
