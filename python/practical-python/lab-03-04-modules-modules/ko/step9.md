# 모듈 로딩

각 모듈은 _한 번만_ 로드되고 실행됩니다. _참고: 반복적인 import 는 이전에 로드된 모듈에 대한 참조를 반환합니다._

`sys.modules`는 로드된 모든 모듈의 딕셔너리입니다.

```python
>>> import sys
>>> sys.modules.keys()
['copy_reg', '__main__', 'site', '__builtin__', 'encodings', 'encodings.encodings', 'posixpath', ...]
>>>
```

**주의:** 모듈의 소스 코드를 변경한 후 `import` 문을 반복하면 흔히 혼란이 발생합니다. 모듈 캐시 `sys.modules` 때문에 반복적인 import 는 변경이 이루어졌더라도 항상 이전에 로드된 모듈을 반환합니다. 수정된 코드를 Python 에 로드하는 가장 안전한 방법은 인터프리터를 종료하고 다시 시작하는 것입니다.
