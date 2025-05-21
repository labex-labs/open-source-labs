# 모듈 다시 로딩 제한 사항 탐색

모듈 다시 로딩은 Python 에서 유용한 기능이지만 클래스를 다룰 때 특히 몇 가지 제한 사항이 있습니다. 이 섹션에서는 이러한 제한 사항을 단계별로 살펴보겠습니다. 이러한 제한 사항을 이해하는 것은 개발 및 프로덕션 환경 모두에서 중요합니다.

1. Python 인터프리터를 다시 시작합니다.
   먼저 Python 인터프리터를 다시 시작해야 합니다. 이 단계는 깨끗한 상태로 시작하기 때문에 중요합니다. 인터프리터를 다시 시작하면 이전에 가져온 모든 모듈과 변수가 지워집니다. 현재 Python 인터프리터를 종료하려면 `exit()` 명령을 사용합니다. 그런 다음 터미널에서 `python3` 명령을 사용하여 새 Python 인터프리터 세션을 시작합니다.

```python
>>> exit()
```

```bash
python3
```

2. 모듈을 가져오고 `Spam` 클래스의 인스턴스를 생성합니다.
   이제 새로운 Python 인터프리터 세션이 있으므로 `simplemod` 모듈을 가져오겠습니다. 모듈을 가져오면 해당 모듈에 정의된 클래스, 함수 및 변수를 사용할 수 있습니다. 모듈을 가져온 후 `Spam` 클래스의 인스턴스를 생성하고 `yow()` 메서드를 호출합니다. 이렇게 하면 클래스의 초기 동작을 확인할 수 있습니다.

```python
>>> import simplemod
Loaded simplemod
>>> s = simplemod.Spam()
>>> s.yow()
Yow!
```

3. 이제 모듈에서 `Spam` 클래스를 수정해 보겠습니다. Python 인터프리터를 종료합니다.
   다음으로 `simplemod` 모듈의 `Spam` 클래스를 변경할 것입니다. 그 전에 Python 인터프리터를 종료해야 합니다. 이는 모듈의 소스 코드를 변경한 다음 해당 변경 사항이 클래스의 동작에 어떤 영향을 미치는지 확인하려는 것이기 때문입니다.

```python
>>> exit()
```

4. WebIDE 에서 `simplemod.py` 파일을 열고 `Spam` 클래스를 수정합니다.
   WebIDE 에서 `simplemod.py` 파일을 엽니다. 여기에는 `simplemod` 모듈의 소스 코드가 있습니다. `Spam` 클래스의 `yow()` 메서드를 수정하여 다른 메시지를 출력합니다. 이 변경 사항은 모듈을 다시 로드한 후 클래스의 동작이 어떻게 변경되는지 관찰하는 데 도움이 됩니다.

```python
# simplemod.py
# ... (leave the rest of the file unchanged)

class Spam:
    def yow(self):
        print('More Yow!')  # Changed from 'Yow!'
```

5. 파일을 저장하고 터미널로 돌아갑니다. Python 인터프리터를 시작하고 새 인스턴스를 생성합니다.
   `simplemod.py` 파일에 변경 사항을 적용한 후 저장합니다. 그런 다음 터미널로 돌아가 새 Python 인터프리터 세션을 시작합니다. `simplemod` 모듈을 다시 가져오고 `Spam` 클래스의 새 인스턴스를 생성합니다. 새 인스턴스의 `yow()` 메서드를 호출하여 업데이트된 동작을 확인합니다.

```bash
python3
```

```python
>>> import simplemod
Loaded simplemod
>>> t = simplemod.Spam()
>>> t.yow()
More Yow!
```

6. 이제 다시 로딩으로 어떤 일이 발생하는지 시연해 보겠습니다.
   모듈 다시 로딩이 어떻게 작동하는지 확인하기 위해 `importlib.reload()` 함수를 사용합니다. 이 함수를 사용하면 이전에 가져온 모듈을 다시 로드할 수 있습니다. 모듈을 다시 로드한 후 `Spam` 클래스에 적용한 변경 사항이 반영되는지 확인합니다.

```python
>>> import importlib
>>> importlib.reload(simplemod)
Loaded simplemod
<module 'simplemod' from 'simplemod.py'>
```

7. Python 을 종료하고 파일을 다시 수정한 다음 두 인스턴스를 모두 테스트합니다.
   Python 인터프리터를 다시 종료합니다. 그런 다음 `simplemod.py` 파일의 `Spam` 클래스를 다시 변경합니다. 그 후 `Spam` 클래스의 이전 및 새 인스턴스를 모두 테스트하여 동작 방식을 확인합니다.

```python
>>> exit()
```

8. `simplemod.py` 파일을 업데이트합니다.
   `simplemod.py` 파일을 다시 열고 `Spam` 클래스의 `yow()` 메서드를 수정하여 다른 메시지를 출력합니다. 이 변경 사항은 모듈 다시 로딩의 제한 사항을 더 잘 이해하는 데 도움이 됩니다.

```python
# simplemod.py
# ... (leave the rest of the file unchanged)

class Spam:
    def yow(self):
        print('Even More Yow!')  # Changed again
```

9. 파일을 저장하고 터미널로 돌아갑니다.
   `simplemod.py` 파일에 대한 변경 사항을 저장하고 터미널로 돌아갑니다. 새 Python 인터프리터 세션을 시작하고 `simplemod` 모듈을 가져온 다음 `Spam` 클래스의 새 인스턴스를 생성합니다. 새 인스턴스의 `yow()` 메서드를 호출하여 업데이트된 동작을 확인합니다.

```bash
python3
```

```python
>>> import simplemod
Loaded simplemod
>>> s = simplemod.Spam()
>>> s.yow()
Even More Yow!

>>> # Exit without closing Python, edit the file
```

10. Python 을 닫지 않고 WebIDE 에서 `simplemod.py`를 열고 변경합니다.
    Python 인터프리터를 닫지 않고 WebIDE 에서 `simplemod.py` 파일을 열고 `Spam` 클래스의 `yow()` 메서드를 다시 변경합니다. 이렇게 하면 모듈을 다시 로드한 후 기존 및 새 인스턴스의 동작이 어떻게 변경되는지 확인할 수 있습니다.

```python
# simplemod.py
# ... (leave the rest of the file unchanged)

class Spam:
    def yow(self):
        print('Super Yow!')  # Changed one more time
```

11. 파일을 저장하고 Python 인터프리터로 돌아갑니다.
    `simplemod.py` 파일에 대한 변경 사항을 저장하고 Python 인터프리터로 돌아갑니다. `importlib.reload()` 함수를 사용하여 `simplemod` 모듈을 다시 로드합니다. 그런 다음 `Spam` 클래스의 이전 및 새 인스턴스를 모두 테스트하여 동작 방식을 확인합니다.

```python
>>> import importlib
>>> importlib.reload(simplemod)
Loaded simplemod
<module 'simplemod' from 'simplemod.py'>

>>> # Try the old instance
>>> s.yow()
Even More Yow!  # Still uses the old implementation

>>> # Create a new instance
>>> t = simplemod.Spam()
>>> t.yow()
Super Yow!  # Uses the new implementation
```

이전 인스턴스 `s`는 여전히 이전 구현을 사용하고 새 인스턴스 `t`는 새 구현을 사용한다는 것을 알 수 있습니다. 이는 모듈을 다시 로드해도 클래스의 기존 인스턴스가 업데이트되지 않기 때문에 발생합니다. 클래스 인스턴스가 생성되면 해당 시점의 클래스 객체에 대한 참조를 저장합니다. 모듈을 다시 로드하면 새 클래스 객체가 생성되지만 기존 인스턴스는 여전히 이전 클래스 객체를 참조합니다.

12. 다른 특이한 동작도 관찰할 수 있습니다.
    `isinstance()` 함수를 사용하여 모듈 다시 로딩의 제한 사항을 더 자세히 관찰할 수 있습니다. 이 함수는 객체가 특정 클래스의 인스턴스인지 확인합니다. 모듈을 다시 로드한 후 이전 인스턴스 `s`는 더 이상 새 `simplemod.Spam` 클래스의 인스턴스로 간주되지 않고 새 인스턴스 `t`는 인스턴스로 간주되는 것을 확인할 수 있습니다.

```python
>>> isinstance(s, simplemod.Spam)
False
>>> isinstance(t, simplemod.Spam)
True
```

이는 다시 로드한 후 `simplemod.Spam`이 `s`를 생성하는 데 사용된 것과 다른 클래스 객체를 참조함을 나타냅니다.

이러한 제한 사항으로 인해 모듈 다시 로딩은 주로 개발 및 디버깅에 유용하며 프로덕션 코드에는 권장되지 않습니다. 프로덕션 환경에서는 클래스의 모든 인스턴스가 동일한 최신 구현을 사용하도록 보장하는 것이 중요합니다. 모듈 다시 로딩은 일관성 없는 동작으로 이어질 수 있으며, 이는 디버깅 및 유지 관리가 어려울 수 있습니다.
