# 기본 인자 (Default Arguments)

때로는 인자를 선택적으로 만들고 싶을 수 있습니다. 이 경우, 함수 정의에서 기본값을 할당하십시오.

```python
def read_prices(filename, debug=False):
    ...
```

기본값이 할당되면, 해당 인자는 함수 호출 시 선택 사항이 됩니다.

```python
d = read_prices('prices.csv')
e = read_prices('prices.dat', True)
```

_참고: 기본값을 가진 인자는 인자 목록의 끝에 나타나야 합니다 (모든 필수 인자는 먼저 옵니다)._
