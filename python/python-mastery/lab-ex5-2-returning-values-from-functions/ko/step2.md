# 선택적 값 반환

프로그래밍에서 함수가 유효한 결과를 생성할 수 없는 경우가 있습니다. 예를 들어, 함수가 입력에서 특정 정보를 추출하도록 되어 있지만 입력이 예상 형식이 아닌 경우입니다. Python 에서 이러한 상황을 처리하는 일반적인 방법은 `None`을 반환하는 것입니다. `None`은 유효한 반환 값이 없음을 나타내는 Python 의 특수한 값입니다.

입력이 예상 기준을 충족하지 않는 경우 함수를 수정하여 처리하는 방법을 살펴보겠습니다. 'name=value' 형식의 라인을 구문 분석하고 이름과 값을 모두 반환하도록 설계된 `parse_line` 함수를 사용합니다.

1. `return_values.py` 파일에서 `parse_line` 함수를 업데이트합니다.

```python
def parse_line(line):
    """
    'name=value' 형식의 라인을 구문 분석하고 이름과 값을 모두 반환합니다.
    라인이 올바른 형식이 아니면 None 을 반환합니다.

    Args:
        line (str): 'name=value' 형식으로 구문 분석할 입력 라인

    Returns:
        tuple or None: (name, value) 를 포함하는 튜플 또는 구문 분석에 실패하면 None
    """
    parts = line.split('=', 1)  # 첫 번째 등호에서 분할
    if len(parts) == 2:
        name = parts[0]
        value = parts[1]
        return (name, value)  # 튜플로 반환
    else:
        return None  # 잘못된 입력에 대해 None 반환
```

이 업데이트된 `parse_line` 함수에서 먼저 `split` 메서드를 사용하여 입력 라인을 첫 번째 등호에서 분할합니다. 결과 목록에 정확히 두 개의 요소가 있으면 라인이 올바른 'name=value' 형식임을 의미합니다. 그런 다음 이름과 값을 추출하여 튜플로 반환합니다. 목록에 두 개의 요소가 없으면 입력이 잘못된 것이므로 `None`을 반환합니다.

2. 업데이트된 함수를 보여주기 위해 테스트 코드를 추가합니다.

```python
# 업데이트된 parse_line 함수 테스트
if __name__ == "__main__":
    # 유효한 입력
    result1 = parse_line('email=guido@python.org')
    print(f"Valid input result: {result1}")

    # 잘못된 입력
    result2 = parse_line('invalid_line_without_equals_sign')
    print(f"Invalid input result: {result2}")

    # 결과를 사용하기 전에 None 확인
    test_line = 'user_info'
    result = parse_line(test_line)
    if result is None:
        print(f"Could not parse the line: '{test_line}'")
    else:
        name, value = result
        print(f"Name: {name}, Value: {value}")
```

이 테스트 코드는 유효한 입력과 잘못된 입력을 모두 사용하여 `parse_line` 함수를 호출합니다. 그런 다음 결과를 출력합니다. `parse_line` 함수의 결과를 사용할 때 먼저 `None`인지 확인합니다. 튜플인 것처럼 `None` 값을 언패킹하려고 하면 오류가 발생하므로 이것이 중요합니다.

3. 파일을 저장하고 실행합니다.

```
python ~/project/return_values.py
```

스크립트를 실행하면 다음과 유사한 출력을 볼 수 있습니다.

```
Valid input result: ('email', 'guido@python.org')
Invalid input result: None
Could not parse the line: 'user_info'
```

**설명:**

- 이제 함수는 라인에 등호가 포함되어 있는지 확인합니다. 이는 등호에서 라인을 분할하고 결과 목록의 길이를 확인하여 수행됩니다.
- 라인에 등호가 포함되어 있지 않으면 구문 분석에 실패했음을 나타내기 위해 `None`을 반환합니다.
- 이러한 함수를 사용할 때는 사용하기 전에 결과가 `None`인지 확인하는 것이 중요합니다. 그렇지 않으면 `None` 값의 요소에 액세스하려고 할 때 오류가 발생할 수 있습니다.

**설계 토론:**
잘못된 입력을 처리하는 또 다른 방법은 예외를 발생시키는 것입니다. 이 접근 방식은 특정 상황에 적합합니다.

1. 잘못된 입력은 실제로 예외적이며 예상되는 경우가 아닙니다. 예를 들어, 입력이 신뢰할 수 있는 소스에서 제공되어야 하고 항상 올바른 형식이어야 하는 경우입니다.
2. 호출자가 오류를 처리하도록 강제하려는 경우. 예외를 발생시키면 프로그램의 정상적인 흐름이 중단되고 호출자는 오류를 명시적으로 처리해야 합니다.
3. 자세한 오류 정보를 제공해야 하는 경우. 예외는 오류에 대한 추가 정보를 전달할 수 있으며, 이는 디버깅에 유용할 수 있습니다.

예외 기반 접근 방식의 예:

```python
def parse_line_with_exception(line):
    """라인을 구문 분석하고 잘못된 입력에 대해 예외를 발생시킵니다."""
    parts = line.split('=', 1)
    if len(parts) != 2:
        raise ValueError(f"Invalid format: '{line}' does not contain '='")
    return (parts[0], parts[1])
```

`None`을 반환할지 예외를 발생시킬지는 애플리케이션의 요구 사항에 따라 다릅니다.

- 결과가 없는 것이 일반적이고 예상되는 경우 `None`을 반환합니다. 예를 들어, 목록에서 항목을 검색할 때 항목이 없을 수 있습니다.
- 실패가 예상치 못하고 정상적인 흐름을 중단해야 하는 경우 예외를 발생시킵니다. 예를 들어, 항상 존재해야 하는 파일에 액세스하려고 할 때입니다.
