# 연습 9.1: 간단한 패키지 만들기

`porty/`라는 디렉토리를 만들고 위의 모든 Python 파일을 그 안에 넣습니다. 또한 빈 `__init__.py` 파일을 생성하여 디렉토리에 넣습니다. 다음과 같은 파일 디렉토리가 있어야 합니다:

    porty/
        __init__.py
        fileparse.py
        follow.py
        pcost.py
        portfolio.py
        report.py
        stock.py
        tableformat.py
        ticker.py
        typedproperty.py

디렉토리에 있는 `__pycache__` 파일을 제거합니다. 이 파일에는 이전의 사전 컴파일된 Python 모듈이 포함되어 있습니다. 우리는 처음부터 시작하고 싶습니다.

패키지 모듈 중 일부를 가져오기를 시도해 봅니다:

```python
>>> import porty.report
>>> import porty.pcost
>>> import porty.ticker
```

이러한 가져오기가 실패하면, 해당 파일로 이동하여 모듈 가져오기를 패키지 상대 가져오기를 포함하도록 수정합니다. 예를 들어, `import fileparse`와 같은 문은 다음과 같이 변경될 수 있습니다:

    # report.py
    from . import fileparse
    ...

`from fileparse import parse_csv`와 같은 문이 있는 경우, 코드를 다음과 같이 변경합니다:

    # report.py
    from .fileparse import parse_csv
    ...
