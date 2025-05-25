# 비교 (Comparisons)

다음 비교/관계 연산자는 숫자와 함께 작동합니다:

    x < y      미만 (Less than)
    x <= y     이하 (Less than or equal)
    x > y      초과 (Greater than)
    x >= y     이상 (Greater than or equal)
    x == y     같음 (Equal to)
    x != y     같지 않음 (Not equal to)

다음 연산자를 사용하여 더 복잡한 부울 표현식을 구성할 수 있습니다:

`and`, `or`, `not`

다음은 몇 가지 예입니다:

```python
if b >= a and b <= c:
    print('b is between a and c')

if not (b < a or b > c):
    print('b is still between a and c')
```
