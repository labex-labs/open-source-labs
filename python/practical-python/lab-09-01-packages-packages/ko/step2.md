# 패키지 (Packages) vs 모듈 (Modules)

더 큰 코드 모음의 경우, 모듈을 패키지로 구성하는 것이 일반적입니다.

```code
# From this
pcost.py
report.py
fileparse.py

# To this
porty/
    __init__.py
    pcost.py
    report.py
    fileparse.py
```

이름을 선택하고 최상위 디렉토리를 만듭니다. 위의 예에서 `porty` (분명히 이 이름을 선택하는 것이 가장 중요한 첫 번째 단계입니다).

`__init__.py` 파일을 디렉토리에 추가합니다. 비어 있을 수 있습니다.

소스 파일을 디렉토리에 넣습니다.
