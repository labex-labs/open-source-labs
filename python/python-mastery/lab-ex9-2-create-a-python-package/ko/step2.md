# 패키지 구조 생성

이제 Python 패키지를 만들 것입니다. 하지만 먼저 Python 패키지가 무엇인지 이해해 봅시다. Python 패키지는 관련 Python 모듈을 단일 디렉토리 계층 구조로 구성하는 방법입니다. 코드를 보다 효과적으로 관리하고 재사용하는 데 도움이 됩니다. Python 패키지를 만들려면 다음 단계를 따라야 합니다.

1. 패키지 이름으로 디렉토리를 만듭니다. 이 디렉토리는 패키지에 속하는 모든 모듈의 컨테이너 역할을 합니다.
2. 이 디렉토리 안에 `__init__.py` 파일을 만듭니다. 이 파일은 Python 이 디렉토리를 패키지로 인식하게 하므로 매우 중요합니다. 패키지를 import 하면 `__init__.py`의 코드가 실행되어 패키지를 초기화하는 데 사용할 수 있습니다.
3. Python 모듈 파일을 이 디렉토리로 이동합니다. 이 단계는 관련 코드가 모두 패키지 내에서 함께 그룹화되도록 합니다.

단계별로 패키지 구조를 만들어 보겠습니다.

1. 먼저 `structly`라는 디렉토리를 만듭니다. 이것이 우리 패키지의 루트 디렉토리가 됩니다.

```bash
mkdir structly
```

2. 다음으로, `structly` 디렉토리 안에 빈 `__init__.py` 파일을 만듭니다.

```bash
touch structly/__init__.py
```

`__init__.py` 파일은 비어 있을 수 있지만, Python 이 디렉토리를 패키지로 취급하려면 필요합니다. 패키지를 import 하면 `__init__.py`의 코드가 실행되어 패키지를 초기화하는 데 사용할 수 있습니다.

3. 이제 Python 모듈 파일을 `structly` 디렉토리로 이동해 보겠습니다. 이 모듈 파일에는 패키지에 포함하려는 함수와 클래스가 포함되어 있습니다.

```bash
mv structure.py validate.py reader.py tableformat.py structly/
```

4. 모든 파일이 올바르게 이동되었는지 확인합니다. `ls -l` 명령을 사용하여 `structly` 디렉토리의 내용을 나열할 수 있습니다.

```bash
ls -l structly/
```

다음 파일이 나열되어야 합니다.

```
__init__.py
reader.py
structure.py
tableformat.py
validate.py
```

이제 기본적인 패키지 구조를 만들었습니다. 디렉토리 계층 구조는 다음과 같아야 합니다.

```
project/
├── portfolio.csv
├── stock.py
└── structly/
    ├── __init__.py
    ├── reader.py
    ├── structure.py
    ├── tableformat.py
    └── validate.py
```

다음 단계에서는 패키지가 올바르게 작동하도록 import 문을 수정합니다.
