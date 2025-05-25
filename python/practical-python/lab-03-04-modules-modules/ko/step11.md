# 모듈 검색 경로

앞서 언급했듯이, `sys.path`에는 검색 경로가 포함되어 있습니다. 필요에 따라 수동으로 조정할 수 있습니다.

```python
import sys
sys.path.append('/project/foo/pyfiles')
```

환경 변수를 통해 경로를 추가할 수도 있습니다.

```python
% env PYTHONPATH=/project/foo/pyfiles python3
Python 3.6.0 (default, Feb 3 2017, 05:53:21)
[GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.38)]
>>> import sys
>>> sys.path
['','/project/foo/pyfiles', ...]
```

일반적으로 모듈 검색 경로를 수동으로 조정할 필요는 없습니다. 그러나 특이한 위치에 있거나 현재 작업 디렉토리에서 쉽게 접근할 수 없는 Python 코드를 import 하려는 경우에 발생할 수 있습니다.

모듈과 관련된 이 연습에서는 적절한 환경에서 Python 을 실행하고 있는지 확인하는 것이 매우 중요합니다. 모듈은 종종 새로운 프로그래머에게 현재 작업 디렉토리 또는 Python 의 경로 설정과 관련된 문제를 제시합니다. 이 과정에서는 모든 코드를 `~/project` 디렉토리에서 작성한다고 가정합니다. 최상의 결과를 얻으려면 인터프리터를 시작할 때 해당 디렉토리에도 있는지 확인해야 합니다. 그렇지 않은 경우 `~/project`가 `sys.path`에 추가되었는지 확인해야 합니다.
