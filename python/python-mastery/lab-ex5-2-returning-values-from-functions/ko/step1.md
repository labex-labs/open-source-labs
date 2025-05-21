# 함수에서 여러 값 반환하기

Python 에서는 함수가 둘 이상의 값을 반환해야 할 때 유용한 해결책이 있습니다: 튜플을 반환하는 것입니다. 튜플은 Python 의 데이터 구조 유형 중 하나입니다. 튜플은 불변 시퀀스 (immutable sequence) 로, 튜플을 생성한 후에는 해당 요소를 변경할 수 없습니다. 튜플은 서로 다른 유형의 여러 값을 한 곳에 보관할 수 있기 때문에 유용합니다.

`name=value` 형식의 구성 라인을 구문 분석하는 함수를 만들어 보겠습니다. 이 함수의 목표는 이 형식의 라인을 가져와 이름과 값을 별도의 항목으로 반환하는 것입니다.

1. 먼저, 새로운 Python 파일을 생성해야 합니다. 이 파일에는 함수와 테스트 코드에 대한 코드가 포함됩니다. 프로젝트 디렉토리에서 `return_values.py`라는 파일을 생성합니다. 터미널에서 다음 명령을 사용하여 이 파일을 생성할 수 있습니다.

```
touch ~/project/return_values.py
```

2. 이제 코드 편집기에서 `return_values.py` 파일을 엽니다. 이 파일 내부에 `parse_line` 함수를 작성합니다. 이 함수는 라인을 입력으로 받아 첫 번째 '=' 기호에서 분할하고 이름과 값을 튜플로 반환합니다.

```python
def parse_line(line):
    """
    'name=value' 형식의 라인을 구문 분석하고 이름과 값을 모두 반환합니다.

    Args:
        line (str): 'name=value' 형식으로 구문 분석할 입력 라인

    Returns:
        tuple: (name, value) 를 포함하는 튜플
    """
    parts = line.split('=', 1)  # 첫 번째 등호에서 분할
    if len(parts) == 2:
        name = parts[0]
        value = parts[1]
        return (name, value)  # 튜플로 반환
```

이 함수에서 `split` 메서드는 입력 라인을 첫 번째 '=' 기호에서 두 부분으로 나눕니다. 라인이 올바른 `name=value` 형식인 경우 이름과 값을 추출하여 튜플로 반환합니다.

3. 함수를 정의한 후, 함수가 예상대로 작동하는지 확인하기 위해 몇 가지 테스트 코드를 추가해야 합니다. 테스트 코드는 샘플 입력을 사용하여 `parse_line` 함수를 호출하고 결과를 출력합니다.

```python
# parse_line 함수 테스트
if __name__ == "__main__":
    result = parse_line('email=guido@python.org')
    print(f"Result as tuple: {result}")

    # 튜플을 별도의 변수로 언패킹
    name, value = parse_line('email=guido@python.org')
    print(f"Unpacked name: {name}")
    print(f"Unpacked value: {value}")
```

테스트 코드에서 먼저 `parse_line` 함수를 호출하고 반환된 튜플을 `result` 변수에 저장합니다. 그런 다음 이 튜플을 출력합니다. 다음으로, 튜플 언패킹 (tuple unpacking) 을 사용하여 튜플의 요소를 `name` 및 `value` 변수에 직접 할당하고 별도로 출력합니다.

4. 함수와 테스트 코드를 작성했으면 `return_values.py` 파일을 저장합니다. 그런 다음 터미널을 열고 다음 명령을 실행하여 Python 스크립트를 실행합니다.

```
python ~/project/return_values.py
```

다음과 유사한 출력을 볼 수 있습니다.

```
Result as tuple: ('email', 'guido@python.org')
Unpacked name: email
Unpacked value: guido@python.org
```

**설명:**

- `parse_line` 함수는 `split` 메서드를 사용하여 입력 문자열을 '=' 문자를 기준으로 분할합니다. 이 메서드는 지정된 구분 기호를 기준으로 문자열을 부분으로 나눕니다.
- `return (name, value)` 구문을 사용하여 두 부분을 튜플로 반환합니다. 튜플은 여러 값을 함께 그룹화하는 방법입니다.
- 함수를 호출할 때 두 가지 옵션이 있습니다. `result` 변수에서와 같이 전체 튜플을 하나의 변수에 저장할 수 있습니다. 또는 `name, value = parse_line(...)` 구문을 사용하여 튜플을 별도의 변수로 직접 "언패킹"할 수 있습니다. 이렇게 하면 개별 값으로 작업하기가 더 쉬워집니다.

튜플로 여러 값을 반환하는 이 패턴은 Python 에서 매우 일반적입니다. 함수가 호출하는 코드에 둘 이상의 정보를 제공할 수 있으므로 함수를 더 다재다능하게 만듭니다.
