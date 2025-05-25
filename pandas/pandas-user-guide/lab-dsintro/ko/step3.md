# DataFrame 생성

다른 기본적인 데이터 구조는 DataFrame 입니다. DataFrame 은 잠재적으로 서로 다른 유형의 열을 가진 2 차원 레이블 데이터 구조입니다.

```python
# Create a DataFrame
df = pd.DataFrame(np.random.randn(6, 4), columns=list('ABCD'))
```
