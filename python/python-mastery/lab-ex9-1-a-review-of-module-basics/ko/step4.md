# from module import 구문 사용

Python 에는 모듈에서 구성 요소를 가져오는 다양한 방법이 있습니다. 이러한 방법 중 하나는 이 섹션에서 살펴볼 `from module import` 구문입니다.

모듈에서 구성 요소를 가져올 때는 깨끗한 상태로 시작하는 것이 좋습니다. 이렇게 하면 이전 상호 작용에서 남은 변수나 설정이 현재 실험을 방해할 수 없도록 보장합니다.

1. 깨끗한 상태를 얻으려면 Python 인터프리터를 다시 시작합니다.

```python
>>> exit()
```

이 명령은 현재 Python 인터프리터 세션을 종료합니다. 종료 후에는 새로운 환경을 보장하기 위해 새 세션을 시작합니다.

```bash
python3
```

이 bash 명령은 새 Python 3 인터프리터 세션을 시작합니다. 이제 깨끗한 Python 환경이 있으므로 모듈에서 구성 요소를 가져오기 시작할 수 있습니다.

2. `from module import` 구문을 사용하여 모듈에서 특정 구성 요소를 가져옵니다.

```python
>>> from simplemod import foo
Loaded simplemod
>>> foo()
x is 42
```

여기서는 `from simplemod import foo` 문을 사용하여 `simplemod` 모듈에서 `foo` 함수만 가져옵니다. `foo` 함수만 요청했지만 전체 `simplemod` 모듈이 로드되었음을 알 수 있습니다. 이는 "Loaded simplemod" 출력으로 표시됩니다. 이러한 이유는 Python 이 `foo` 함수에 액세스하기 위해 전체 모듈을 로드해야 하기 때문입니다.

3. `from module import`를 사용하는 경우 모듈 자체에 액세스할 수 없습니다.

```python
>>> simplemod.foo()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'simplemod' is not defined
```

`from module import` 구문을 사용하면 지정된 구성 요소만 네임스페이스로 직접 가져옵니다. 모듈 이름 자체는 가져오지 않습니다. 따라서 `simplemod.foo()`에 액세스하려고 하면 Python 은 해당 방식으로 가져오지 않았기 때문에 `simplemod`를 인식하지 못합니다.

4. 여러 구성 요소를 한 번에 가져올 수 있습니다.

```python
>>> from simplemod import x, foo
>>> x
42
>>> foo()
x is 42
```

`from module import` 구문을 사용하면 단일 문에서 모듈에서 여러 구성 요소를 가져올 수 있습니다. 여기서는 `simplemod` 모듈에서 변수 `x`와 함수 `foo`를 모두 가져옵니다. 가져온 후에는 코드에서 이러한 구성 요소에 직접 액세스할 수 있습니다.

5. 모듈에서 변수를 가져올 때 모듈의 변수에 대한 링크가 아닌 객체에 대한 새 참조를 생성합니다.

```python
>>> x = 13  # Change the local variable x
>>> x
13
>>> foo()
x is 42  # The function still uses the module's x, not your local x
```

모듈에서 변수를 가져올 때 기본적으로 로컬 네임스페이스에서 동일한 객체에 대한 새 참조를 생성합니다. 따라서 로컬 변수 `x`를 `13`으로 변경해도 `simplemod` 모듈 내부의 `x` 변수에는 영향을 미치지 않습니다. `foo()` 함수는 여전히 모듈의 `x` 변수 (`42`) 를 참조합니다. 이 개념을 이해하는 것은 코드에서 혼란을 피하는 데 중요합니다.
