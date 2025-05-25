# 사용자 정의 눈금 표시기 함수 정의

다음으로, 사용자 정의 눈금 표시기 함수를 정의해야 합니다. 사용자 정의 눈금 표시기 함수는 값과 눈금 위치의 두 가지 인수를 사용하고 형식화된 눈금 레이블을 반환합니다. 이 경우, 눈금 레이블을 백만 달러 단위로 형식화합니다.

```python
def millions(x, pos):
    """The two arguments are the value and tick position."""
    return f'${x*1e-6:1.1f}M'
```
