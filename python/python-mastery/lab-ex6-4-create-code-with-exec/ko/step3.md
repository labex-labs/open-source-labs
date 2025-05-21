# Python 표준 라이브러리가 exec() 를 사용하는 방법 검토

Python 에서 표준 라이브러리는 다양한 유용한 함수와 모듈을 제공하는 미리 작성된 코드의 강력한 모음입니다. 이러한 함수 중 하나는 `exec()`로, Python 코드를 동적으로 생성하고 실행하는 데 사용할 수 있습니다. 동적으로 코드를 생성한다는 것은 하드 코딩된 코드를 갖는 대신 프로그램 실행 중에 즉석에서 코드를 생성하는 것을 의미합니다.

`collections` 모듈의 `namedtuple` 함수는 `exec()`를 사용하는 표준 라이브러리의 잘 알려진 예입니다. `namedtuple`은 속성 이름과 인덱스 모두를 사용하여 해당 요소에 액세스할 수 있는 특수한 종류의 튜플입니다. 완전한 클래스 정의를 작성하지 않고도 간단한 데이터 보관 클래스를 만드는 데 유용한 도구입니다.

`namedtuple`이 어떻게 작동하고 내부적으로 `exec()`를 사용하는지 살펴보겠습니다. 먼저, Python 셸을 엽니다. 터미널에서 다음 명령을 실행하여 이 작업을 수행할 수 있습니다. 이 명령은 Python 코드를 직접 실행할 수 있는 Python 인터프리터를 시작합니다.

```bash
python3
```

이제 `namedtuple` 함수를 사용하는 방법을 살펴보겠습니다. 다음 코드는 `namedtuple`을 생성하고 해당 요소에 액세스하는 방법을 보여줍니다.

```python
>>> from collections import namedtuple
>>> Stock = namedtuple('Stock', ['name', 'shares', 'price'])
>>> s = Stock('GOOG', 100, 490.1)
>>> s.name
'GOOG'
>>> s.shares
100
>>> s[1]  # namedtuples also support indexing
100
```

위의 코드에서 먼저 `collections` 모듈에서 `namedtuple` 함수를 가져옵니다. 그런 다음 `name`, `shares`, `price` 필드가 있는 `Stock`이라는 새 `namedtuple` 유형을 생성합니다. `Stock` `namedtuple`의 인스턴스 `s`를 생성하고 속성 이름 (`s.name`, `s.shares`) 과 인덱스 (`s[1]`) 를 모두 사용하여 해당 요소에 액세스합니다.

이제 `namedtuple`이 어떻게 구현되었는지 살펴보겠습니다. `inspect` 모듈을 사용하여 소스 코드를 볼 수 있습니다. `inspect` 모듈은 모듈, 클래스, 메서드 등과 같은 라이브 객체에 대한 정보를 얻기 위해 몇 가지 유용한 함수를 제공합니다.

```python
>>> import inspect
>>> from collections import namedtuple
>>> print(inspect.getsource(namedtuple))
```

이 코드를 실행하면 많은 양의 코드가 출력됩니다. 자세히 살펴보면 `namedtuple`이 `exec()` 함수를 사용하여 클래스를 동적으로 생성한다는 것을 알 수 있습니다. 수행하는 작업은 클래스 정의에 대한 Python 코드를 포함하는 문자열을 구성하는 것입니다. 그런 다음 `exec()`를 사용하여 이 문자열을 Python 코드로 실행합니다.

이 접근 방식은 `namedtuple`이 런타임에 사용자 지정 필드 이름으로 클래스를 생성할 수 있으므로 매우 강력합니다. 필드 이름은 `namedtuple` 함수에 전달하는 인수에 의해 결정됩니다. 이것은 `exec()`를 사용하여 코드를 동적으로 생성할 수 있는 실제 예입니다.

`namedtuple`의 구현에 대해 주목해야 할 몇 가지 주요 사항은 다음과 같습니다.

1. 문자열 형식을 사용하여 클래스 정의를 구성합니다. 문자열 형식은 문자열 템플릿에 값을 삽입하는 방법입니다. `namedtuple`의 경우 이를 사용하여 올바른 필드 이름으로 클래스 정의를 만듭니다.
2. 필드 이름의 유효성을 처리합니다. 즉, 제공하는 필드 이름이 유효한 Python 식별자인지 확인합니다. 그렇지 않은 경우 적절한 오류가 발생합니다.
3. docstring 및 메서드와 같은 추가 기능을 제공합니다. Docstring 은 클래스 또는 함수의 목적과 사용법을 문서화하는 문자열입니다. `namedtuple`은 생성하는 클래스에 유용한 docstring 및 메서드를 추가합니다.
4. `exec()`를 사용하여 생성된 코드를 실행합니다. 이것은 클래스 정의를 포함하는 문자열을 실제 Python 클래스로 바꾸는 핵심 단계입니다.

이 패턴은 `create_init()` 메서드에서 구현한 것과 유사하지만 더 정교한 수준입니다. `namedtuple` 구현은 강력하고 사용자 친화적인 인터페이스를 제공하기 위해 더 복잡한 시나리오와 예외 사례를 처리해야 합니다.
