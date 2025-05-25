# 헬퍼 함수 정의

두 개의 헬퍼 함수를 정의합니다. 첫 번째 함수인 `to_ordinal`은 정수를 서수 문자열로 변환합니다 (예: 2 -> '2nd'). 두 번째 함수인 `format_score`는 테스트 이름과 측정 단위 (있는 경우) 를 두 줄로 나누어 오른쪽 y 축에 대한 점수 레이블을 생성합니다.

```python
def to_ordinal(num):
    suffixes = {str(i): v
                for i, v in enumerate(['th', 'st', 'nd', 'rd', 'th',
                                       'th', 'th', 'th', 'th', 'th'])}
    v = str(num)
    if v in {'11', '12', '13'}:
        return v + 'th'
    return v + suffixes[v[-1]]

def format_score(score):
    return f'{score.value}\n{score.unit}' if score.unit else str(score.value)
```
