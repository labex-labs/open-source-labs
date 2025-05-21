# 데이터 구조로서의 클로저

Python 에서 클로저는 데이터를 캡슐화 (encapsulate) 하는 강력한 방법을 제공합니다. 캡슐화는 데이터를 비공개로 유지하고 이에 대한 접근을 제어하는 것을 의미합니다. 클로저를 사용하면 클래스나 전역 변수를 사용하지 않고도 개인 데이터를 관리하고 수정하는 함수를 만들 수 있습니다. 전역 변수는 코드의 어느 곳에서나 접근하고 수정할 수 있으므로 예상치 못한 동작을 초래할 수 있습니다. 반면에 클래스는 더 복잡한 구조를 필요로 합니다. 클로저는 데이터 캡슐화를 위한 더 간단한 대안을 제공합니다.

이 개념을 시연하기 위해 `counter.py`라는 파일을 만들어 보겠습니다.

1. WebIDE 를 열고 `/home/labex/project` 디렉토리에 `counter.py`라는 새 파일을 만듭니다. 여기에서 클로저 기반 카운터를 정의하는 코드를 작성합니다.

2. 파일에 다음 코드를 추가합니다.

```python
def counter(value):
    """
    증가 및 감소 함수가 있는 카운터를 생성합니다.

    인수:
        value: 카운터의 초기 값

    반환값:
        두 개의 함수: 카운터를 증가시키는 함수 하나, 감소시키는 함수 하나
    """
    def incr():
        nonlocal value
        value += 1
        return value

    def decr():
        nonlocal value
        value -= 1
        return value

    return incr, decr
```

이 코드에서 `counter()`라는 함수를 정의합니다. 이 함수는 초기 `value`를 인수로 받습니다. `counter()` 함수 내부에서 `incr()`과 `decr()`이라는 두 개의 내부 함수를 정의합니다. 이 내부 함수는 동일한 `value` 변수에 대한 접근을 공유합니다. `nonlocal` 키워드는 Python 에게 외부 범위 (enclosing scope, `counter()` 함수) 에서 `value` 변수를 수정하려는 것을 알려주는 데 사용됩니다. `nonlocal` 키워드가 없으면 Python 은 외부 범위의 `value`를 수정하는 대신 내부 함수 내에 새로운 지역 변수를 생성합니다.

3. 이제 이 동작을 확인하기 위해 테스트 파일을 만들어 보겠습니다. 다음 내용으로 `test_counter.py`라는 새 파일을 만듭니다.

```python
from counter import counter

# 0 에서 시작하는 카운터 생성
up, down = counter(0)

# 카운터를 여러 번 증가시킵니다.
print("Incrementing the counter:")
print(up())  # Should print 1
print(up())  # Should print 2
print(up())  # Should print 3

# 카운터를 감소시킵니다.
print("\nDecrementing the counter:")
print(down())  # Should print 2
print(down())  # Should print 1
```

이 테스트 파일에서 먼저 `counter.py` 파일에서 `counter()` 함수를 가져옵니다. 그런 다음 `counter(0)`을 호출하고 반환된 함수를 `up`과 `down`으로 언패킹하여 0 에서 시작하는 카운터를 생성합니다. 그런 다음 `up()` 함수를 여러 번 호출하여 카운터를 증가시키고 결과를 출력합니다. 그 후, `down()` 함수를 호출하여 카운터를 감소시키고 결과를 출력합니다.

4. 터미널에서 다음 명령을 실행하여 테스트 파일을 실행합니다.

```bash
python3 test_counter.py
```

다음 출력을 볼 수 있습니다.

```
Incrementing the counter:
1
2
3

Decrementing the counter:
2
1
```

여기에는 클래스 정의가 포함되어 있지 않다는 점에 유의하십시오. `up()` 및 `down()` 함수는 전역 변수도 인스턴스 속성도 아닌 공유 값을 조작하고 있습니다. 이 값은 클로저에 저장되어 `counter()`에서 반환된 함수만 접근할 수 있습니다.

이것은 클로저를 데이터 구조로 사용하는 방법의 예입니다. 캡슐화된 변수 `value`는 함수 호출 간에 유지되며, 이에 접근하는 함수에 대해 비공개입니다. 즉, 코드의 다른 부분에서는 이 `value` 변수에 직접 접근하거나 수정할 수 없으므로 데이터 보호 수준을 제공합니다.
