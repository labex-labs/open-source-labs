# 검증자 유형 수집

Python 에서 검증자 (validators) 는 데이터가 특정 기준을 충족하는지 확인하는 데 도움이 되는 클래스입니다. 이 실험의 첫 번째 작업은 기본 `Validator` 클래스를 수정하여 모든 하위 클래스를 수집할 수 있도록 하는 것입니다. 왜 이렇게 해야 할까요? 모든 검증자 하위 클래스를 수집함으로써 모든 검증자 유형을 포함하는 네임스페이스 (namespace) 를 생성할 수 있습니다. 나중에 이 네임스페이스를 `Structure` 클래스에 주입하여 다양한 검증자를 더 쉽게 관리하고 사용할 수 있도록 할 것입니다.

이제 코드를 시작해 보겠습니다. `validate.py` 파일을 엽니다. 터미널에서 다음 명령을 사용하여 열 수 있습니다.

```bash
code validate.py
```

파일이 열리면 `Validator` 클래스에 클래스 수준 딕셔너리와 `__init_subclass__()` 메서드를 추가해야 합니다. 클래스 수준 딕셔너리는 모든 검증자 하위 클래스를 저장하는 데 사용되며, `__init_subclass__()` 메서드는 현재 클래스의 하위 클래스가 정의될 때마다 호출되는 Python 의 특수 메서드입니다.

클래스 정의 바로 뒤에 다음 코드를 `Validator` 클래스에 추가합니다.

```python
# Add this to the Validator class in validate.py
validators = {}  # Dictionary to collect all validator subclasses

@classmethod
def __init_subclass__(cls):
    """Register each validator subclass in the validators dictionary"""
    Validator.validators[cls.__name__] = cls
```

코드를 추가한 후 수정된 `Validator` 클래스는 다음과 같아야 합니다.

```python
class Validator:
    validators = {}  # Dictionary to collect all validator subclasses

    @classmethod
    def __init_subclass__(cls):
        """Register each validator subclass in the validators dictionary"""
        Validator.validators[cls.__name__] = cls

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        self.validate(value)
        instance.__dict__[self.name] = value

    def validate(self, value):
        pass
```

이제 `String` 또는 `PositiveInteger`와 같은 새로운 검증자 유형이 정의될 때마다 Python 은 자동으로 `__init_subclass__()` 메서드를 호출합니다. 그런 다음 이 메서드는 클래스 이름을 키로 사용하여 새 검증자 하위 클래스를 `validators` 딕셔너리에 추가합니다.

코드가 작동하는지 테스트해 보겠습니다. `validators` 딕셔너리의 내용을 확인하는 간단한 Python 스크립트를 생성합니다. 터미널에서 다음 명령을 실행할 수 있습니다.

```bash
python3 -c "from validate import Validator; print(Validator.validators)"
```

모든 것이 제대로 작동하면 다음과 유사한 출력이 표시되어 모든 검증자 유형과 해당 클래스를 보여줍니다.

```
{'Typed': <class 'validate.Typed'>, 'Positive': <class 'validate.Positive'>, 'NonEmpty': <class 'validate.NonEmpty'>, 'String': <class 'validate.String'>, 'Integer': <class 'validate.Integer'>, 'Float': <class 'validate.Float'>, 'PositiveInteger': <class 'validate.PositiveInteger'>, 'PositiveFloat': <class 'validate.PositiveFloat'>, 'NonEmptyString': <class 'validate.NonEmptyString'>}
```

이제 모든 검증자 유형을 포함하는 딕셔너리가 있으므로 다음 단계에서 메타클래스를 생성하는 데 사용할 수 있습니다.
