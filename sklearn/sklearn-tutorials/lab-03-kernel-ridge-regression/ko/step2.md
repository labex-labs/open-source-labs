# 합성 데이터 생성

다음으로, 작업할 합성 데이터를 생성합니다. 사인 함수 타겟 함수를 생성하고 일부 랜덤 노이즈를 추가합니다.

```python
# 입력 데이터 생성
np.random.seed(0)
X = np.sort(5 * np.random.rand(100, 1), axis=0)
y = np.sin(X).ravel()
y += 0.5 * (0.5 - np.random.rand(y.size))
```
