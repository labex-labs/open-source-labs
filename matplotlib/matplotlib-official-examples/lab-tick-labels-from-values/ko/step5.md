# 형식 지정 함수 생성

눈금 값에서 눈금 레이블을 결정하는 형식 지정 함수를 생성합니다. 눈금 값이 `xs` 범위 내의 정수이면 `labels` 목록에서 해당 레이블이 반환됩니다. 그렇지 않으면 빈 문자열이 반환됩니다.

```python
def format_fn(tick_val, tick_pos):
    if int(tick_val) in xs:
        return labels[int(tick_val)]
    else:
        return ''
```
