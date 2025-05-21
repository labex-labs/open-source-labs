# inspect 모듈 사용

Python 에서는 표준 라이브러리에 매우 유용한 `inspect` 모듈이 포함되어 있습니다. 이 모듈은 Python 의 라이브 객체에 대한 정보를 수집하는 데 도움이 되는 탐정 도구와 같습니다. 라이브 객체는 모듈, 클래스 및 함수와 같은 것일 수 있습니다. 객체의 속성을 수동으로 파고들어 정보를 찾는 대신, `inspect` 모듈은 함수의 속성을 이해하는 데 더 체계적이고 높은 수준의 방법을 제공합니다.

이 모듈이 어떻게 작동하는지 탐구하기 위해 동일한 Python 대화형 셸을 계속 사용해 보겠습니다.

## 함수 시그니처 (Function Signatures)

`inspect.signature()` 함수는 유용한 도구입니다. 함수를 전달하면 `Signature` 객체를 반환합니다. 이 객체는 함수의 매개변수에 대한 중요한 세부 정보를 담고 있습니다.

예를 들어 보겠습니다. `add`라는 함수가 있다고 가정해 보겠습니다. `inspect.signature()` 함수를 사용하여 시그니처를 얻을 수 있습니다.

```python
import inspect
sig = inspect.signature(add)
print(sig)
```

이 코드를 실행하면 출력은 다음과 같습니다.

```
(x, y)
```

이 출력은 함수가 허용할 수 있는 매개변수를 알려주는 함수의 시그니처를 보여줍니다.

## 매개변수 세부 정보 검사

한 단계 더 나아가 함수의 각 매개변수에 대한 더 자세한 정보를 얻을 수 있습니다.

```python
print(sig.parameters)
```

이 코드의 출력은 다음과 같습니다.

```
OrderedDict([('x', <Parameter "x">), ('y', <Parameter "y">)])
```

함수의 매개변수는 정렬된 딕셔너리에 저장됩니다. 때로는 매개변수의 이름만 관심 있을 수 있습니다. 이 정렬된 딕셔너리를 튜플로 변환하여 매개변수 이름만 추출할 수 있습니다.

```python
param_names = tuple(sig.parameters)
print(param_names)
```

출력은 다음과 같습니다.

```
('x', 'y')
```

## 개별 매개변수 검사

각 개별 매개변수를 자세히 살펴볼 수도 있습니다. 다음 코드는 함수의 각 매개변수를 반복하고 이에 대한 몇 가지 중요한 세부 정보를 출력합니다.

```python
for name, param in sig.parameters.items():
    print(f"Parameter: {name}")
    print(f"  Kind: {param.kind}")
    print(f"  Default: {param.default if param.default is not param.empty else 'No default'}")
```

이 코드는 각 매개변수에 대한 세부 정보를 보여줍니다. 매개변수의 종류 (위치 매개변수인지, 키워드 매개변수인지 등) 와 기본값이 있는 경우 기본값을 알려줍니다.

`inspect` 모듈에는 함수 인트로스펙션 (function introspection) 을 위한 다른 많은 유용한 함수가 있습니다. 다음은 몇 가지 예입니다.

- `inspect.getdoc(obj)`: 이 함수는 객체에 대한 문서 문자열을 검색합니다. 문서 문자열은 프로그래머가 객체가 수행하는 작업을 설명하기 위해 작성하는 메모와 같습니다.
- `inspect.getfile(obj)`: 객체가 정의된 파일을 찾는 데 도움이 됩니다. 객체의 소스 코드를 찾고 싶을 때 매우 유용할 수 있습니다.
- `inspect.getsource(obj)`: 이 함수는 객체의 소스 코드를 가져옵니다. 객체가 정확히 어떻게 구현되었는지 확인할 수 있습니다.
