# 타사 테스트 도구 (Third Party Test Tools)

내장된 `unittest` 모듈은 어디에서나 사용할 수 있다는 장점이 있습니다. 즉, Python 의 일부입니다. 그러나 많은 프로그래머는 또한 이것이 상당히 장황하다고 생각합니다. 널리 사용되는 대안은 [pytest](https://docs.pytest.org/en/latest/)입니다. pytest 를 사용하면 테스트 파일이 다음과 같이 단순화됩니다.

```python
# test_simple.py
import simple

def test_simple():
    assert simple.add(2,2) == 4

def test_str():
    assert simple.add('hello','world') == 'helloworld'
```

테스트를 실행하려면 `python -m pytest`와 같은 명령을 입력하기만 하면 됩니다. 그러면 모든 테스트를 찾아 실행합니다. 이 모듈은 `pip install pytest`를 사용하여 설치할 수 있습니다.

이 예제보다 `pytest`에는 훨씬 더 많은 기능이 있지만, 사용해보기로 결정했다면 일반적으로 시작하기가 매우 쉽습니다.

이 연습에서는 Python 의 `unittest` 모듈 사용의 기본 메커니즘을 탐구합니다.

이전 연습에서는 `Stock` 클래스를 포함하는 `stock.py` 파일을 작성했습니다. 이 연습에서는 유형 속성을 포함하는 Exercise 7.9 에 대해 작성된 코드를 사용한다고 가정합니다. 어떤 이유로 작동하지 않는 경우, `Solutions/7_9`에서 솔루션을 작업 디렉토리로 복사할 수 있습니다.
