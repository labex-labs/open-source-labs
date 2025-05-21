# 모듈 로딩 동작 이해

Python 에서 모듈이 로드되는 방식에는 몇 가지 흥미로운 특징이 있습니다. 이 단계에서는 Python 이 모듈 로딩을 관리하는 방식을 이해하기 위해 이러한 동작을 살펴보겠습니다.

1. 먼저, 동일한 Python 인터프리터 세션 내에서 모듈을 다시 가져오려고 할 때 어떤 일이 발생하는지 살펴보겠습니다. Python 인터프리터를 시작하면 Python 코드를 실행할 수 있는 작업 공간을 여는 것과 같습니다. 모듈을 가져온 후 다시 가져오면 모듈이 다시 로드되는 것처럼 보일 수 있지만 그렇지 않습니다.

```python
>>> import simplemod
```

이번에는 "Loaded simplemod" 출력이 표시되지 않는 것을 알 수 있습니다. 이는 **Python 이 인터프리터 세션당 한 번만 모듈을 로드하기** 때문입니다. 후속 `import` 문은 모듈을 다시 로드하지 않습니다. Python 은 이미 모듈을 로드했음을 기억하므로 다시 로드하는 과정을 거치지 않습니다.

2. 모듈을 가져온 후에는 내부 변수를 수정할 수 있습니다. Python 의 모듈은 변수, 함수 및 클래스를 담는 컨테이너와 같습니다. 모듈을 가져오면 다른 Python 객체와 마찬가지로 해당 변수에 액세스하고 변경할 수 있습니다.

```python
>>> simplemod.x
42
>>> simplemod.x = 13
>>> simplemod.x
13
>>> simplemod.foo()
x is 13
```

여기서는 먼저 `simplemod` 모듈의 변수 `x`의 값을 확인합니다. 초기 값은 `42`입니다. 그런 다음 값을 `13`으로 변경하고 변경 사항이 적용되었는지 확인합니다. 모듈에서 `foo` 함수를 호출하면 `x`의 새 값을 반영합니다.

3. 모듈을 다시 가져와도 변수에 대한 변경 사항이 재설정되지 않습니다. 모듈을 다시 가져오려고 시도하더라도 Python 은 다시 로드하지 않으므로 변수에 대한 변경 사항이 유지됩니다.

```python
>>> import simplemod
>>> simplemod.x
13
```

4. 모듈을 강제로 다시 로드하려면 `importlib.reload()` 함수를 사용해야 합니다. 때로는 모듈의 코드를 변경하고 해당 변경 사항이 즉시 적용되는 것을 확인하고 싶을 수 있습니다. `importlib.reload()` 함수를 사용하면 그렇게 할 수 있습니다.

```python
>>> import importlib
>>> importlib.reload(simplemod)
Loaded simplemod
<module 'simplemod' from 'simplemod.py'>
>>> simplemod.x
42
>>> simplemod.foo()
x is 42
```

모듈이 다시 로드되었고 `x`의 값이 `42`로 재설정되었습니다. 이는 모듈이 소스 코드에서 다시 로드되었고 모든 변수가 원래대로 초기화되었음을 보여줍니다.

5. Python 은 `sys.modules` 딕셔너리에 로드된 모든 모듈을 추적합니다. 이 딕셔너리는 현재 인터프리터 세션 동안 로드된 모든 모듈에 대한 정보를 Python 이 저장하는 레지스트리 역할을 합니다.

```python
>>> 'simplemod' in sys.modules
True
>>> sys.modules['simplemod']
<module 'simplemod' from 'simplemod.py'>
```

모듈 이름이 `sys.modules` 딕셔너리에 있는지 확인하여 모듈이 로드되었는지 확인할 수 있습니다. 그리고 모듈 이름을 키로 사용하여 딕셔너리에 액세스하면 모듈에 대한 정보를 얻을 수 있습니다.

6. 다음 가져오기에서 Python 이 다시 로드하도록 하려면 이 딕셔너리에서 모듈을 제거할 수 있습니다. `sys.modules` 딕셔너리에서 모듈을 제거하면 Python 은 이미 모듈을 로드했음을 잊어버립니다. 따라서 다음에 가져오려고 하면 Python 은 소스 코드에서 다시 로드합니다.

```python
>>> del sys.modules['simplemod']
>>> import simplemod
Loaded simplemod
>>> simplemod.x
42
```

`sys.modules`에서 모듈이 제거되었기 때문에 모듈이 다시 로드되었습니다. 이는 모듈 코드의 최신 버전을 사용하고 있는지 확인하는 또 다른 방법입니다.
