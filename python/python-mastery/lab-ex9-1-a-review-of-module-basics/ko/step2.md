# 모듈 가져오기 및 사용

이제 모듈을 만들었으므로, 이를 가져와서 구성 요소를 사용하는 방법을 이해할 차례입니다. Python 에서 모듈은 Python 정의와 문을 포함하는 파일입니다. 모듈을 가져오면 해당 모듈 내에 정의된 모든 함수, 클래스 및 변수에 액세스할 수 있습니다. 이를 통해 코드를 재사용하고 프로그램을 보다 효과적으로 구성할 수 있습니다.

1. 먼저 WebIDE 에서 새 터미널을 열어야 합니다. 이 터미널은 Python 명령을 실행할 수 있는 작업 공간 역할을 합니다. 새 터미널을 열려면 "Terminal" > "New Terminal"을 클릭합니다.

2. 터미널이 열리면 Python 인터프리터를 시작해야 합니다. Python 인터프리터는 Python 코드를 읽고 실행하는 프로그램입니다. 이를 시작하려면 터미널에 다음 명령을 입력하고 Enter 키를 누릅니다.

```bash
python3
```

3. 이제 Python 인터프리터가 실행 중이므로 모듈을 가져올 수 있습니다. Python 에서는 `import` 문을 사용하여 현재 프로그램에 모듈을 가져옵니다. Python 인터프리터에 다음 명령을 입력합니다.

```python
>>> import simplemod
Loaded simplemod
```

출력에 "Loaded simplemod"가 나타나는 것을 알 수 있습니다. 이는 `simplemod` 모듈의 `print` 문이 모듈이 로드될 때 실행되기 때문입니다. Python 은 모듈을 가져올 때 해당 모듈의 모든 최상위 코드를 실행하며, 여기에는 모든 `print` 문이 포함됩니다.

4. 모듈을 가져온 후에는 점 표기법을 사용하여 해당 구성 요소에 액세스할 수 있습니다. 점 표기법은 Python 에서 객체의 속성 (변수 및 함수) 에 액세스하는 방법입니다. 이 경우 모듈은 객체이고 해당 함수, 변수 및 클래스는 속성입니다. `simplemod` 모듈의 다양한 구성 요소에 액세스하는 방법의 몇 가지 예는 다음과 같습니다.

```python
>>> simplemod.x
42
>>> simplemod.foo()
x is 42
>>> spam_instance = simplemod.Spam()
>>> spam_instance.yow()
Yow!
```

첫 번째 줄에서는 `simplemod` 모듈에 정의된 변수 `x`에 액세스합니다. 두 번째 줄에서는 `simplemod` 모듈에서 함수 `foo`를 호출합니다. 세 번째 및 네 번째 줄에서는 `simplemod` 모듈에 정의된 `Spam` 클래스의 인스턴스를 생성하고 해당 메서드 `yow`를 호출합니다.

5. 때로는 모듈을 가져오려고 할 때 `ImportError`가 발생할 수 있습니다. 이 오류는 Python 이 가져오려는 모듈을 찾을 수 없을 때 발생합니다. Python 이 모듈을 어디에서 찾고 있는지 확인하려면 `sys.path` 변수를 검사할 수 있습니다. `sys.path` 변수는 Python 이 모듈을 찾을 때 검색하는 디렉토리 목록입니다. Python 인터프리터에 다음 명령을 입력합니다.

```python
>>> import sys
>>> sys.path
['', '/usr/lib/python310.zip', '/usr/lib/python3.10', '/usr/lib/python3.10/lib-dynload', '/usr/local/lib/python3.10/dist-packages', '/usr/lib/python3/dist-packages']
```

목록의 첫 번째 요소 (빈 문자열) 는 현재 작업 디렉토리를 나타냅니다. 이것이 Python 이 `simplemod.py` 파일을 찾는 곳입니다. 모듈이 `sys.path`에 나열된 디렉토리 중 하나에 없으면 Python 은 이를 찾을 수 없으며 `ImportError`가 발생합니다. `simplemod.py` 파일이 현재 작업 디렉토리 또는 `sys.path`의 다른 디렉토리 중 하나에 있는지 확인하십시오.
